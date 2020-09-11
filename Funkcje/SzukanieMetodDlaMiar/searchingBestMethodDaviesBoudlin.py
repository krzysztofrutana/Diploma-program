import numpy as np
from numpy import unique, float64
from sklearn.cluster import DBSCAN, AgglomerativeClustering
from sklearn.metrics import davies_bouldin_score
from tqdm import tqdm

from Funkcje.PomocniczeDlaMetod.DBSCAN_KNN import DB_SCAN
from Funkcje.PomocniczeDlaMetod.kmeans_with_metric import kmeans
from Funkcje.minimumMaximumOtherUsefull import minimum


def szukanieDaviesBoudlin(dane, daneoryginalne, maxIter, ileKlastrow):
    dane = dane.astype(float64)
    distance = ['euclidean', 'cityblock', 'cosine']
    if dane.shape[1] < 2:
        return -1

    najlepszyWynikDaviesBoudlinDBScan = 10
    najlepszaMetrykaDaviesBoudlinDBSCAN = ""
    najlepszyParametrSilhouetteDBScan = 0

    najlepszyWynikDaviesBoudlinKMeans = 10
    najlepszaMetrykaDaviesBoudlinKMeans = ""
    optymalnaLiczbaKlastrowDaviesBoudlinKMeans = 0

    najlepszyWynikDaviesBoudlinAC = 10
    najlepszaMetrykaDaviesBoudlinAC = ""
    optymalnaLiczbaKlastrowDaviesBoudlinAC = 0


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
                score_DaviesBoudlin_DB = davies_bouldin_score(daneoryginalne, db.labels_)
                if score_DaviesBoudlin_DB < najlepszyWynikDaviesBoudlinDBScan:
                    najlepszyWynikDaviesBoudlinDBScan = score_DaviesBoudlin_DB
                    najlepszaMetrykaDaviesBoudlinDBSCAN = i
                    najlepszyParametrSilhouetteDBScan = eps
        except Exception as inst:
            print(inst)

        for k in tqdm(range(2, ileKlastrow+1, 1), desc= "Test ilosci klastrow", dynamic_ncols=True):

            try:
                KM = kmeans(dane, n_clusters=k, metric=i, maxiter=maxIter, verbose=0)
                labelsKM = KM[1]
                score_DaviesBoudlin_KM = davies_bouldin_score(daneoryginalne, labelsKM)

                if score_DaviesBoudlin_KM < najlepszyWynikDaviesBoudlinKMeans:
                    najlepszyWynikDaviesBoudlinKMeans = score_DaviesBoudlin_KM
                    najlepszaMetrykaDaviesBoudlinKMeans = i
                    optymalnaLiczbaKlastrowDaviesBoudlinKMeans = k
            except Exception as inst:
                print(inst)

            try:
                ac = AgglomerativeClustering(n_clusters=k, affinity=i, linkage="average").fit(dane)
                labelsAC = ac.labels_
                score_DaviesBoudlin_AC = davies_bouldin_score(daneoryginalne, labelsAC)

                if score_DaviesBoudlin_AC < najlepszyWynikDaviesBoudlinAC:
                    najlepszyWynikDaviesBoudlinAC = score_DaviesBoudlin_AC
                    najlepszaMetrykaDaviesBoudlinAC = i
                    optymalnaLiczbaKlastrowDaviesBoudlinAC = k
            except Exception as inst:
                print(inst)



    najlepszyWynikDaviesBoudlin = minimum(najlepszyWynikDaviesBoudlinDBScan, najlepszyWynikDaviesBoudlinKMeans, najlepszyWynikDaviesBoudlinAC)

    if najlepszyWynikDaviesBoudlin == najlepszyWynikDaviesBoudlinDBScan:
        return {"Metoda": "DBScan", "Metryka": najlepszaMetrykaDaviesBoudlinDBSCAN, "eps/k": najlepszyParametrSilhouetteDBScan,
                "Wynik DaviesBoudlin": round(najlepszyWynikDaviesBoudlinDBScan,2), "Liczba koniecznych wymiarów": dane.shape[1]}
    if najlepszyWynikDaviesBoudlin == najlepszyWynikDaviesBoudlinKMeans:
        return {"Metoda": "KMeans", "Metryka": najlepszaMetrykaDaviesBoudlinKMeans, "eps/k": optymalnaLiczbaKlastrowDaviesBoudlinKMeans,
                "Wynik DaviesBoudlin": round(najlepszyWynikDaviesBoudlinKMeans,2), "Liczba koniecznych wymiarów": dane.shape[1]}
    if najlepszyWynikDaviesBoudlin == najlepszyWynikDaviesBoudlinAC:
        return {"Metoda": "Agglomerative", "Metryka": najlepszaMetrykaDaviesBoudlinAC, "eps/k": optymalnaLiczbaKlastrowDaviesBoudlinAC,
                "Wynik DaviesBoudlin": round(najlepszyWynikDaviesBoudlinAC,2), "Liczba koniecznych wymiarów": dane.shape[1]}
