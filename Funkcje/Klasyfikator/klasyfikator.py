import pandas as pd
from numpy import float64, unique
import numpy as np
from sklearn import preprocessing, neighbors
from sklearn.cluster import AgglomerativeClustering, DBSCAN
from sklearn.linear_model import LinearRegression
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from sklearn.tree import DecisionTreeRegressor
from Funkcje.PomocniczeDlaMetod.kmeans_with_metric import kmeans


def klasyfikacja(dane, cechy, klasyfikatorMetodaMetryka, klasyfikatorParametr,  miara):

    cechyDoKlasyfikacji = pd.DataFrame.from_dict([cechy], orient='columns')

    klasyfikacjaMetodaMetryka = klasyfikatorMetodaMetryka.predict(cechyDoKlasyfikacji)[0]
    cechyDoKlasyfikacji['Metoda_metryka'] =  int(klasyfikacjaMetodaMetryka)
    cechyDoKlasyfikacji['Parametr'] =  klasyfikatorParametr.predict(cechyDoKlasyfikacji)[0]

    metoda_metryka = cechyDoKlasyfikacji.iloc[0,cechyDoKlasyfikacji.columns.get_loc('Metoda_metryka')]
    parametr = cechyDoKlasyfikacji.iloc[0,cechyDoKlasyfikacji.columns.get_loc('Parametr')]

    daneKlasyfikacja = dane.copy()
    daneKlasyfikacja = daneKlasyfikacja.astype(float64)

    if metoda_metryka == 11:
        db = DBSCAN(eps=parametr, metric='euclidean').fit(daneKlasyfikacja)
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        if miara in 'silhouette':
            if len(unique(db.labels_)) > 1:
                score = silhouette_score(dane, db.labels_, metric='euclidean')
        elif miara in 'daviesBoudlin':
            if len(unique(db.labels_)) > 1:
                score = davies_bouldin_score(dane, db.labels)
        elif miara in 'calinskiHarabasz':
            if len(unique(db.labels_)) > 1:
                score = calinski_harabasz_score(dane, db.labels)
        return 'DBScan', 'euclidean', parametr, score

    elif metoda_metryka == 12:
        db = DBSCAN(eps=parametr, metric='cityblock').fit(daneKlasyfikacja)
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        if miara in 'silhouette':
            if len(unique(db.labels_)) > 1:
                score = silhouette_score(dane, db.labels_, metric='cityblock')
        elif miara in 'daviesBoudlin':
            if len(unique(db.labels_)) > 1:
                score = davies_bouldin_score(dane, db.labels)
        elif miara in 'calinskiHarabasz':
            if len(unique(db.labels_)) > 1:
                score = calinski_harabasz_score(dane, db.labels)

        return 'DBScan', 'cityblock', parametr, score

    elif metoda_metryka == 13:
        db = DBSCAN(eps=parametr, metric='cosine').fit(daneKlasyfikacja)
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        if miara in 'silhouette':
            if len(unique(db.labels_)) > 1:
                score = silhouette_score(dane, db.labels_, metric='cosine')
        elif miara in 'daviesBoudlin':
            if len(unique(db.labels_)) > 1:
                score = davies_bouldin_score(dane, db.labels)
        elif miara in 'calinskiHarabasz':
            if len(unique(db.labels_)) > 1:
                score = calinski_harabasz_score(dane, db.labels)

        return 'DBScan', 'cosine', parametr, score

    elif metoda_metryka == 21:
        KM = kmeans(daneKlasyfikacja, n_clusters=int(round(parametr)), metric='euclidean', maxiter=1000, verbose=0)
        labelsKM = KM[1]
        if miara in 'silhouette':
            score = silhouette_score(dane, labelsKM, metric='euclidean')
        elif miara in 'daviesBoudlin':
            score = davies_bouldin_score(dane, labelsKM)
        elif miara in 'calinskiHarabasz':
            score = calinski_harabasz_score(dane, labelsKM)

        return 'KMeans', 'euclidean', int(round(parametr)), score

    elif metoda_metryka == 22:
        KM = kmeans(daneKlasyfikacja, n_clusters=int(round(parametr)), metric='cityblock', maxiter=1000, verbose=0)
        labelsKM = KM[1]
        if miara in 'silhouette':
            score = silhouette_score(dane, labelsKM, metric='cityblock')
        elif miara in 'daviesBoudlin':
            score = davies_bouldin_score(dane, labelsKM)
        elif miara in 'calinskiHarabasz':
            score = calinski_harabasz_score(dane, labelsKM)

        return 'KMeans', 'cityblock', int(round(parametr)), score

    elif metoda_metryka == 23:
        KM = kmeans(daneKlasyfikacja, n_clusters=int(round(parametr)), metric='cosine', maxiter=1000, verbose=0)
        labelsKM = KM[1]
        if miara in 'silhouette':
            score = silhouette_score(dane, labelsKM, metric='cosine')
        elif miara in 'daviesBoudlin':
            score = davies_bouldin_score(dane, labelsKM)
        elif miara in 'calinskiHarabasz':
            score = calinski_harabasz_score(dane, labelsKM)

        return 'KMeans', 'cosine', int(round(parametr)), score

    elif metoda_metryka == 31:
        ac = AgglomerativeClustering(n_clusters=int(round(parametr)), affinity='euclidean', linkage="average").fit(daneKlasyfikacja)
        labelsAC = ac.labels_
        if miara in 'silhouette':
            score = silhouette_score(dane, labelsAC, metric='euclidean')
        elif miara in 'daviesBoudlin':
            score = davies_bouldin_score(dane, labelsAC)
        elif miara in 'calinskiHarabasz':
            score = calinski_harabasz_score(dane, labelsAC)

        return 'Agglomerative', 'euclidean', int(round(parametr)), score

    elif metoda_metryka == 32:
        ac = AgglomerativeClustering(n_clusters=int(round(parametr)), affinity='cityblock', linkage="average").fit(daneKlasyfikacja)
        labelsAC = ac.labels_
        if miara in 'silhouette':
            score = silhouette_score(dane, labelsAC, metric='cityblock')
        elif miara in 'daviesBoudlin':
            score = davies_bouldin_score(dane, labelsAC)
        elif miara in 'calinskiHarabasz':
            score = calinski_harabasz_score(dane, labelsAC)

        return 'Agglomerative', 'cityblock', int(round(parametr)), score

    elif metoda_metryka == 33:
        ac = AgglomerativeClustering(n_clusters=int(round(parametr)), affinity='cosine', linkage="average").fit(daneKlasyfikacja)
        labelsAC = ac.labels_
        if miara in 'silhouette':
            score = silhouette_score(dane, labelsAC, metric='cosine')
        elif miara in 'daviesBoudlin':
            score = davies_bouldin_score(dane, labelsAC)
        elif miara in 'calinskiHarabasz':
            score = calinski_harabasz_score(dane, labelsAC)

        return 'Agglomerative', 'cosine', int(round(parametr)), score
