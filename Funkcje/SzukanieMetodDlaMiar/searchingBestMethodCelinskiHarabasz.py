from numpy import unique, float64
import numpy as np
from sklearn.cluster import DBSCAN, AgglomerativeClustering
from sklearn.metrics import calinski_harabasz_score
from tqdm import tqdm
from Funkcje.PomocniczeDlaMetod.DBSCAN_KNN import DB_SCAN
from Funkcje.PomocniczeDlaMetod.kmeans_with_metric import kmeans
from Funkcje.minimumMaximumOtherUsefull import maximum


def szukanieCH(dane, daneoryginalne, maxIter, ileKlastrow):
    dane = dane.astype(float64)
    distance = ['euclidean', 'cityblock', 'cosine']
    if dane.shape[1] < 2:
        return -1
    najlepszyWynikCHDBScan = 0
    najlepszaMetrykaDBSCAN = ""
    najlepszyParametrSilhouetteDBScan = 0

    najlepszyWynikCHKMeans = 0
    najlepszaMetrykaCHKMeans = ""
    optymalnaLiczbaKlastrowCHKMeans = 0

    najlepszyWynikCHAC = 0
    najlepszaMetrykaCHAC = ""
    optymalnaLiczbaKlastrowCHAC = 0

    for i in distance:
        print("Test dla " + i)
        try:
            daneDB = dane.copy()
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
                score_CH_DB = calinski_harabasz_score(daneoryginalne, db.labels_)
                if score_CH_DB > najlepszyWynikCHDBScan:
                    najlepszyWynikCHDBScan = score_CH_DB
                    najlepszaMetrykaDBSCAN = i
                    najlepszyParametrSilhouetteDBScan = eps
        except Exception as inst:
            print(inst)

        for k in tqdm(range(2, ileKlastrow+1, 1), desc= "Test ilosci klastrow", dynamic_ncols=True):
            try:
                daneKM = dane.copy()
                KM = kmeans(dane, n_clusters=k, metric=i, maxiter=maxIter, verbose=0)
                labelsKM = KM[1]
                score_CH_KM = calinski_harabasz_score(daneoryginalne, labelsKM)

                if score_CH_KM > najlepszyWynikCHKMeans:
                    najlepszyWynikCHKMeans = score_CH_KM
                    najlepszaMetrykaCHKMeans = i
                    optymalnaLiczbaKlastrowCHKMeans = k
            except Exception as inst:
                print(inst)

            try:
                daneAC = dane.copy()
                ac = AgglomerativeClustering(n_clusters=k, affinity=i, linkage="average").fit(dane)
                labelsAC = ac.labels_
                score_CH_AC = calinski_harabasz_score(daneoryginalne, labelsAC)

                if score_CH_AC > najlepszyWynikCHAC:
                    najlepszyWynikCHAC = score_CH_AC
                    najlepszaMetrykaCHAC = i
                    optymalnaLiczbaKlastrowCHAC = k
            except Exception as inst:
                print(inst)

    najlepszyWynikCH = maximum(najlepszyWynikCHDBScan, najlepszyWynikCHKMeans, najlepszyWynikCHAC)

    if najlepszyWynikCH == najlepszyWynikCHDBScan:
        return {"Metoda":"DBScan", "Metryka": najlepszaMetrykaDBSCAN,"eps/k":najlepszyParametrSilhouetteDBScan, "Wynik CelinskiHarabasz" : round(najlepszyWynikCHDBScan,2),
                "Liczba koniecznych wymiarów" : dane.shape[1]}
    if najlepszyWynikCH == najlepszyWynikCHKMeans:
        return {"Metoda": "KMeans", "Metryka": najlepszaMetrykaCHKMeans, "eps/k": optymalnaLiczbaKlastrowCHKMeans,
                "Wynik CelinskiHarabasz": round(najlepszyWynikCHKMeans,2), "Liczba koniecznych wymiarów" : dane.shape[1]}
    if najlepszyWynikCH == najlepszyWynikCHAC:
        return {"Metoda": "Agglomerative", "Metryka": najlepszaMetrykaCHAC,
                "eps/k": optymalnaLiczbaKlastrowCHAC,
                "Wynik CelinskiHarabasz": round(najlepszyWynikCHAC,2), "Liczba koniecznych wymiarów" : dane.shape[1]}
