from kneed import KneeLocator
from numpy import unique, float64
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from tqdm import tqdm

from Funkcje.PomocniczeDlaMetod.DBSCAN_KNN import DB_SCAN
from Funkcje.PomocniczeDlaMetod.kmeans_with_metric import kmeans
from Funkcje.minimumMaximumOtherUsefull import maximum


def szukanieSilhouette(dane, daneoryginalne, maxIter, ileKlastrow):
    dane = dane.astype(float64)
    distance = ['euclidean', 'cityblock', 'cosine']
    if dane.shape[1] < 2:
        return -1
    najlepszyWynikSilhouetteDBScan = -1
    najlepszaMetrykaSilhouetteDBSCAN = ""
    najlepszyParametrSilhouetteDBScan = 0

    najlepszyWynikSilhouetteKMeans = -1
    najlepszaMetrykaSilhouetteKMeans = ""
    optymalnaLiczbaKlastrowSilhouetteKMeans = 0

    najlepszyWynikSilhouetteAC = -1
    najlepszaMetrykaSilhouetteAC = ""
    optymalnaLiczbaKlastrowSilhouetteAC = 0


    for i in distance:
        print("Test dla " + i)
        try:
            dbscanKNN = DB_SCAN("Wariant" + str(dane))
            eps = dbscanKNN.KNNdist_plot(dane, 3, i)
            if eps > 10:
                eps = round(eps)
            elif eps <= 10 and eps > 3:
                eps = round(eps, 1)
            elif eps <= 3:
                eps = round(eps, 2)
            elif eps <= 1:
                eps = round(eps, 4)
            elif eps <= 0.5:
                eps = round(eps, 6)
            elif eps <= 0.2:
                eps = eps
            db = DBSCAN(eps=eps, metric=i).fit(dane)
            core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
            core_samples_mask[db.core_sample_indices_] = True
            if len(unique(db.labels_)) > 1:
                score_silhouette_DB = silhouette_score(daneoryginalne, db.labels_, metric=i)
                if score_silhouette_DB > najlepszyWynikSilhouetteDBScan:
                    najlepszyWynikSilhouetteDBScan = score_silhouette_DB
                    najlepszaMetrykaSilhouetteDBSCAN = i
                    najlepszyParametrSilhouetteDBScan = eps
        except Exception as inst:
            print(inst)

        silhouette_kmeans = []
        silhouette_ac = []
        silhouette_kmeans_klastry = []
        silhouette_ac_klastry = []
        for k in tqdm(range(2, ileKlastrow+1, 1), desc= "Test ilosci klastrow", dynamic_ncols=True):
            try:
                if i is 'cosine':
                    daneNormalized = pd.DataFrame(dane)
                    daneNormalized = preprocessing.normalize(daneNormalized, norm='l2')

                    KM = kmeans(daneNormalized, n_clusters=k, metric=i, maxiter=maxIter, verbose=0)
                    labelsKM = KM[1]
                    score_silhouette_KM = silhouette_score(daneoryginalne, labelsKM, metric=i)
                    silhouette_kmeans.append(score_silhouette_KM)
                    silhouette_kmeans_klastry.append(k)
                else:
                    KM = kmeans(dane, n_clusters=k, metric=i, maxiter=maxIter, verbose=0)
                    labelsKM = KM[1]
                    score_silhouette_KM = silhouette_score(daneoryginalne, labelsKM, metric=i)
                    silhouette_kmeans.append(score_silhouette_KM)
                    silhouette_kmeans_klastry.append(k)
            except Exception as inst:
                print(inst)

            try:
                ac = AgglomerativeClustering(n_clusters=k, affinity=i, linkage="average").fit(dane)
                labelsAC = ac.labels_
                score_silhouette_AC = silhouette_score(daneoryginalne, labelsAC, metric=i)
                silhouette_ac.append(score_silhouette_AC)
                silhouette_ac_klastry.append(k)
            except Exception as inst:
                print(inst)
        try:
            if len(silhouette_kmeans) > 0:
                kneedleKM = KneeLocator(silhouette_kmeans_klastry, silhouette_kmeans, S=1.0, curve='convex',
                                        direction='decreasing',
                                        interp_method='polynomial')
                if kneedleKM.knee_y > najlepszyWynikSilhouetteKMeans:
                    najlepszyWynikSilhouetteKMeans = kneedleKM.knee_y
                    optymalnaLiczbaKlastrowSilhouetteKMeans = kneedleKM.knee
                    najlepszaMetrykaSilhouetteKMeans = i
        except Exception as inst:
            print(inst)
            pass
        try:
            kneedleAC = KneeLocator(silhouette_ac_klastry, silhouette_ac, S=1.0, curve='convex', direction='decreasing',
                                    interp_method='polynomial')

            if kneedleAC.knee_y > najlepszyWynikSilhouetteAC:
                najlepszyWynikSilhouetteAC = kneedleAC.knee_y
                optymalnaLiczbaKlastrowSilhouetteAC = kneedleAC.knee
                najlepszaMetrykaSilhouetteAC = i
        except Exception as inst:
            print(inst)
            pass

    najlepszyWynikSilhouette = maximum(najlepszyWynikSilhouetteDBScan, najlepszyWynikSilhouetteKMeans, najlepszyWynikSilhouetteAC)


    if najlepszyWynikSilhouette == najlepszyWynikSilhouetteDBScan:
        return {"Metoda":"DBScan", "Metryka": najlepszaMetrykaSilhouetteDBSCAN,"eps/k":najlepszyParametrSilhouetteDBScan, "Wynik Silhouette" : round(najlepszyWynikSilhouetteDBScan,2),
                "Liczba koniecznych wymiarów" : dane.shape[1]}
    if najlepszyWynikSilhouette == najlepszyWynikSilhouetteKMeans:
        return {"Metoda": "KMeans", "Metryka": najlepszaMetrykaSilhouetteKMeans, "eps/k": optymalnaLiczbaKlastrowSilhouetteKMeans,
                "Wynik Silhouette": round(najlepszyWynikSilhouetteKMeans,2), "Liczba koniecznych wymiarów" : dane.shape[1]}
    if najlepszyWynikSilhouette == najlepszyWynikSilhouetteAC:
        return {"Metoda": "Agglomerative", "Metryka": najlepszaMetrykaSilhouetteAC,
                "eps/k": optymalnaLiczbaKlastrowSilhouetteAC,
                "Wynik Silhouette": round(najlepszyWynikSilhouetteAC,2), "Liczba koniecznych wymiarów" : dane.shape[1]}
