import pandas as pd
from sklearn.gaussian_process import GaussianProcessClassifier, GaussianProcessRegressor
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.neural_network import MLPClassifier

from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier


def nauka(miara):

    konfiguracja = pd.read_csv('Funkcje/Klasyfikator/properties.csv',header=0, index_col=0)

    if miara in 'silhouette':
        rezultatyBF = pd.read_csv("TabeleTreningowe/Rezultaty Silhouette.csv")
    elif miara in 'daviesBoudlin':
        rezultatyBF = pd.read_csv("TabeleTreningowe/Rezultaty DaviesBoudlin.csv")
    elif miara in 'calinskiHarabasz':
        rezultatyBF = pd.read_csv("TabeleTreningowe/Rezultaty CelinskiHarabasz.csv")
    else:
        print("Nieznana miara")


    X_trainMetodaMetryka = rezultatyBF[rezultatyBF.columns[0:48]].copy()
    X_trainParametr = rezultatyBF[rezultatyBF.columns[0:49]].copy()

    y_trainMetodaMetryka = pd.DataFrame(rezultatyBF[rezultatyBF.columns[48]]).copy()
    y_trainParametr = pd.DataFrame(rezultatyBF[rezultatyBF.columns[49]]).copy()

    for index,row in y_trainMetodaMetryka.iterrows():
            if row[0] in 'DBScan euclidean':
                row[0] = 11
            elif row[0] in 'DBScan cityblock':
                row[0] = 12
            elif row[0] in 'DBScan cosine':
                row[0] = 13
            elif row[0] in 'KMeans euclidean':
                row[0] = 21
            elif row[0] in 'KMeans cityblock':
                row[0] = 22
            elif row[0] in 'KMeans cosine':
                row[0] = 23
            elif row[0] in 'Agglomerative euclidean':
                row[0] = 31
            elif row[0] in 'Agglomerative cityblock':
                row[0] = 32
            elif row[0] in 'Agglomerative cosine':
                row[0] = 33

    X_trainParametr['Metoda_metryka'] = y_trainMetodaMetryka['Metoda_metryka'].copy()
    y_trainMetodaMetryka = y_trainMetodaMetryka.astype(int)

    #silhouette
    if miara in 'silhouette':
        max_depth = konfiguracja.loc['Silhouette_klasyfikacja', 'max_depth']
        klMetodaMetryka = DecisionTreeClassifier(criterion = konfiguracja.loc['Silhouette_klasyfikacja', 'criterion'],
                                                 max_depth=konfiguracja.loc['Silhouette_klasyfikacja', 'max_depth'],
                                                 random_state=konfiguracja.loc['Silhouette_klasyfikacja', 'random_state'],
                                                 min_samples_leaf = konfiguracja.loc['Silhouette_klasyfikacja', 'min_samples_leaf'],
                                                 min_samples_split = konfiguracja.loc['Silhouette_klasyfikacja', 'min_samples_split'],
                                                 splitter =konfiguracja.loc['Silhouette_klasyfikacja', 'splitter'])
        klMetodaMetryka.fit(X_trainMetodaMetryka, y_trainMetodaMetryka)
        regrParametr = DecisionTreeRegressor(criterion = konfiguracja.loc['Silhouette_regresja', 'criterion'],
                                                 max_depth=konfiguracja.loc['Silhouette_regresja', 'max_depth'],
                                                 random_state=konfiguracja.loc['Silhouette_regresja', 'random_state'],
                                                 min_samples_leaf = konfiguracja.loc['Silhouette_regresja', 'min_samples_leaf'],
                                                 min_samples_split = konfiguracja.loc['Silhouette_regresja', 'min_samples_split'],
                                                 splitter =konfiguracja.loc['Silhouette_regresja', 'splitter'])
        regrParametr.fit(X_trainParametr, y_trainParametr)
    elif miara in 'daviesBoudlin':
        klMetodaMetryka = DecisionTreeClassifier(criterion = konfiguracja.loc['DaviesBouldin_klasyfikacja', 'criterion'],
                                                 max_depth=konfiguracja.loc['DaviesBouldin_klasyfikacja', 'max_depth'],
                                                 random_state=konfiguracja.loc['DaviesBouldin_klasyfikacja', 'random_state'],
                                                 min_samples_leaf = konfiguracja.loc['DaviesBouldin_klasyfikacja', 'min_samples_leaf'],
                                                 min_samples_split = konfiguracja.loc['DaviesBouldin_klasyfikacja', 'min_samples_split'],
                                                 splitter =konfiguracja.loc['DaviesBouldin_klasyfikacja', 'splitter'])
        klMetodaMetryka.fit(X_trainMetodaMetryka, y_trainMetodaMetryka)

        regrParametr = DecisionTreeRegressor(criterion = konfiguracja.loc['DaviesBouldin_regresja', 'criterion'],
                                                 max_depth=konfiguracja.loc['DaviesBouldin_regresja', 'max_depth'],
                                                 random_state=konfiguracja.loc['DaviesBouldin_regresja', 'random_state'],
                                                 min_samples_leaf = konfiguracja.loc['DaviesBouldin_regresja', 'min_samples_leaf'],
                                                 min_samples_split = konfiguracja.loc['DaviesBouldin_regresja', 'min_samples_split'],
                                                 splitter =konfiguracja.loc['DaviesBouldin_regresja', 'splitter'])
        regrParametr.fit(X_trainParametr, y_trainParametr)
    elif miara in 'calinskiHarabasz':
        klMetodaMetryka = DecisionTreeClassifier(criterion = konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'criterion'],
                                                 max_depth=konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'max_depth'],
                                                 random_state=konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'random_state'],
                                                 min_samples_leaf = konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'min_samples_leaf'],
                                                 min_samples_split = konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'min_samples_split'],
                                                 splitter =konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'splitter'])
        klMetodaMetryka.fit(X_trainMetodaMetryka, y_trainMetodaMetryka)

        regrParametr = DecisionTreeRegressor(criterion = konfiguracja.loc['CalinskiHarabasz_regresja', 'criterion'],
                                                 max_depth=konfiguracja.loc['CalinskiHarabasz_regresja', 'max_depth'],
                                                 random_state=konfiguracja.loc['CalinskiHarabasz_regresja', 'random_state'],
                                                 min_samples_leaf = konfiguracja.loc['CalinskiHarabasz_regresja', 'min_samples_leaf'],
                                                 min_samples_split = konfiguracja.loc['CalinskiHarabasz_regresja', 'min_samples_split'],
                                                 splitter =konfiguracja.loc['CalinskiHarabasz_regresja', 'splitter'])
        regrParametr.fit(X_trainParametr, y_trainParametr)

    return klMetodaMetryka, regrParametr


def naukaTestMetodaMetryka(X_train, y_train, czySilhouette, czyDaviesBouldin, czyCalinskiHarabasz):

    konfiguracja = pd.read_csv('Funkcje/Klasyfikator/properties.csv', header=0, index_col=0)

    for index,row in y_train.iteritems():
            if row in 'DBScan euclidean':
                y_train[index] = 11
            elif row in 'DBScan cityblock':
                y_train[index] = 12
            elif row in 'DBScan cosine':
                y_train[index] = 13
            elif row in 'KMeans euclidean':
                y_train[index] = 21
            elif row in 'KMeans cityblock':
                y_train[index] = 22
            elif row in 'KMeans cosine':
                y_train[index] = 23
            elif row in 'Agglomerative euclidean':
                y_train[index] = 31
            elif row in 'Agglomerative cityblock':
                y_train[index] = 32
            elif row in 'Agglomerative cosine':
                y_train[index] = 33

    y_train = y_train.astype(int)


    #SIlhouette
    #best
    if czySilhouette:
        #37
        klMetodaMetryka = DecisionTreeClassifier(criterion = konfiguracja.loc['Silhouette_klasyfikacja', 'criterion'],
                                                 max_depth=konfiguracja.loc['Silhouette_klasyfikacja', 'max_depth'],
                                                 random_state=konfiguracja.loc['Silhouette_klasyfikacja', 'random_state'],
                                                 min_samples_leaf = konfiguracja.loc['Silhouette_klasyfikacja', 'min_samples_leaf'],
                                                 min_samples_split = konfiguracja.loc['Silhouette_klasyfikacja', 'min_samples_split'],
                                                 splitter =konfiguracja.loc['Silhouette_klasyfikacja', 'splitter'])
        klMetodaMetryka.fit(X_train, y_train)

        #35
        # regrMetodaMetryka = MLPClassifier(max_iter=1300,alpha=0.01, random_state=0, hidden_layer_sizes=300,
                                            # solver='lbfgs', learning_rate='constant', activation='tanh')
        # regrMetodaMetryka.fit(X_train, y_train)

        #22
        # regrMetodaMetryka = KNeighborsClassifier(n_neighbors=17,algorithm='auto', weights='uniform', leaf_size=10 )
        # regrMetodaMetryka.fit(X_train, y_train)


    if czyDaviesBouldin:
        # #38 Davies Bouldin
        klMetodaMetryka = DecisionTreeClassifier(criterion = konfiguracja.loc['DaviesBouldin_klasyfikacja', 'criterion'],
                                                 max_depth=konfiguracja.loc['DaviesBouldin_klasyfikacja', 'max_depth'],
                                                 random_state=konfiguracja.loc['DaviesBouldin_klasyfikacja', 'random_state'],
                                                 min_samples_leaf = konfiguracja.loc['DaviesBouldin_klasyfikacja', 'min_samples_leaf'],
                                                 min_samples_split = konfiguracja.loc['DaviesBouldin_klasyfikacja', 'min_samples_split'],
                                                 splitter =konfiguracja.loc['DaviesBouldin_klasyfikacja', 'splitter'])
        klMetodaMetryka.fit(X_train, y_train)
        # 37
        # regrMetodaMetryka = KNeighborsClassifier(n_neighbors = 9,  weights='uniform', algorithm='auto', leaf_size = 10)
        # regrMetodaMetryka.fit(X_train, y_train)
        # 27
        # regrMetodaMetryka = MLPClassifier(max_iter=1300,alpha=0.01, random_state=0, hidden_layer_sizes=300, solver='sgd', learning_rate='constant', activation='tanh')
        # regrMetodaMetryka.fit(X_train, y_train)



    if czyCalinskiHarabasz:
         # 27 Calinski Harabasz
        klMetodaMetryka = DecisionTreeClassifier(criterion = konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'criterion'],
                                                 max_depth=konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'max_depth'],
                                                 random_state=konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'random_state'],
                                                 min_samples_leaf = konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'min_samples_leaf'],
                                                 min_samples_split = konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'min_samples_split'],
                                                 splitter =konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'splitter'])
        klMetodaMetryka.fit(X_train, y_train)
        #
        # regrMetodaMetryka = KNeighborsClassifier(n_neighbors = 14,  weights='uniform', algorithm='auto', leaf_size = 10)
        # regrMetodaMetryka.fit(X_train, y_train)
        #33

        # klMetodaMetryka = MLPClassifier(max_iter=1300,alpha=0.01, random_state=0, hidden_layer_sizes=300, solver='lbfgs', learning_rate='constant', activation='tanh')
        # klMetodaMetryka.fit(X_train, y_train)





    return klMetodaMetryka


def naukaTestParametr(X_train, y_train, czySilhouette, czyDaviesBouldin, czyCalinskiHarabasz):

    konfiguracja = pd.read_csv('Funkcje/Klasyfikator/properties.csv', header=0, index_col=0)

    temp = X_train[X_train.columns[-1]]

    for index, row in temp.iteritems():
        if row in 'DBScan euclidean':
            temp[index] = 11
        elif row in 'DBScan cityblock':
            temp[index] = 12
        elif row in 'DBScan cosine':
            temp[index] = 13
        elif row in 'KMeans euclidean':
            temp[index] = 21
        elif row in 'KMeans cityblock':
            temp[index] = 22
        elif row in 'KMeans cosine':
            temp[index] = 23
        elif row in 'Agglomerative euclidean':
            temp[index] = 31
        elif row in 'Agglomerative cityblock':
            temp[index] = 32
        elif row in 'Agglomerative cosine':
            temp[index] = 33

    X_train['Metoda_metryka'] = temp.copy()


    if czySilhouette:
        regrParametr = DecisionTreeRegressor(criterion = konfiguracja.loc['Silhouette_regresja', 'criterion'],
                                                 max_depth=konfiguracja.loc['Silhouette_regresja', 'max_depth'],
                                                 random_state=konfiguracja.loc['Silhouette_regresja', 'random_state'],
                                                 min_samples_leaf = konfiguracja.loc['Silhouette_regresja', 'min_samples_leaf'],
                                                 min_samples_split = konfiguracja.loc['Silhouette_regresja', 'min_samples_split'],
                                                 splitter =konfiguracja.loc['Silhouette_regresja', 'splitter'])
        regrParametr.fit(X_train, y_train)

        # regrParametr = KNeighborsRegressor(algorithm='auto', leaf_size=10, n_neighbors=19, weights='uniform')
        # regrParametr.fit(X_train, y_train)

    elif czyDaviesBouldin:
        #15%
        regrParametr = DecisionTreeRegressor(criterion = konfiguracja.loc['DaviesBouldin_regresja', 'criterion'],
                                                 max_depth=konfiguracja.loc['DaviesBouldin_regresja', 'max_depth'],
                                                 random_state=konfiguracja.loc['DaviesBouldin_regresja', 'random_state'],
                                                 min_samples_leaf = konfiguracja.loc['DaviesBouldin_regresja', 'min_samples_leaf'],
                                                 min_samples_split = konfiguracja.loc['DaviesBouldin_regresja', 'min_samples_split'],
                                                 splitter =konfiguracja.loc['DaviesBouldin_regresja', 'splitter'])
        regrParametr.fit(X_train, y_train)

        #26%
        # regrParametr = KNeighborsRegressor(algorithm='brute', leaf_size=10, n_neighbors=10, weights='distance')
        # regrParametr.fit(X_train, y_train)

    elif czyCalinskiHarabasz:
        #23
        regrParametr = DecisionTreeRegressor(criterion = konfiguracja.loc['CalinskiHarabasz_regresja', 'criterion'],
                                                 max_depth=konfiguracja.loc['CalinskiHarabasz_regresja', 'max_depth'],
                                                 random_state=konfiguracja.loc['CalinskiHarabasz_regresja', 'random_state'],
                                                 min_samples_leaf = konfiguracja.loc['CalinskiHarabasz_regresja', 'min_samples_leaf'],
                                                 min_samples_split = konfiguracja.loc['CalinskiHarabasz_regresja', 'min_samples_split'],
                                                 splitter =konfiguracja.loc['CalinskiHarabasz_regresja', 'splitter'])
        regrParametr.fit(X_train, y_train)

        # regrParametr = KNeighborsRegressor(algorithm='brute', leaf_size=10, n_neighbors=7, weights='distance')
        # regrParametr.fit(X_train, y_train)


    return regrParametr
