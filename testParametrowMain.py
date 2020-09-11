import threading

from PySide2.QtWidgets import QWidget, QMessageBox, QApplication
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
import sys
from Klasy.PandasModel import PandasModel

from sklearn.neural_network import MLPClassifier
from forms.testParametrow import Ui_FormTestParametrow
from sklearn.model_selection import GridSearchCV, LeaveOneOut


class MyStdout:
    def __init__(self, buffer):
        self.buffer = buffer

    def write(self, string):
        if string:
            self.buffer.append(string)
            QApplication.processEvents()


class TestParametrow(QWidget):

    tabelaBazowa = None
    klasyfikatorMetodaMetryka = None
    klasyfikatorParametr = None

    def __init__(self, czySilhouette, czyDaviesBouldin, czyCalinskiHarabasz):
        super(TestParametrow, self).__init__()
        self.ui = Ui_FormTestParametrow()
        self.ui.setupUi(self)
        self.show()
        self.czySilhouette = czySilhouette
        self.czyCalinskiHarabasz = czyCalinskiHarabasz
        self.czyDaviesBouldin = czyDaviesBouldin

        self.konfiguracja = pd.read_csv('Funkcje/Klasyfikator/properties.csv', header=0, index_col=0)

        klasyfikatory = ["Klasyfikator metody i metryki", "Klasyfikator parametru"]
        self.ui.comboBoxKlasyfikatory.addItems(klasyfikatory)
        self.ui.comboBoxKlasyfikatory.setCurrentIndex(0)
        self.ui.btnPokazTabele.clicked.connect(lambda: self.pokazTabele())
        self.ui.btnTestuj.clicked.connect(lambda: self.testGreadSearchCV())

        self.wczytajTabele()

        sys.stdout = MyStdout(self.ui.txtWyniki)
        sys.stderr = MyStdout(self.ui.txtWyniki)
        # while True:
        #     QApplication.processEvents()

    def wczytajTabele(self):
        rezultatyBF = pd.DataFrame()
        if self.czySilhouette:
            rezultatyBF = pd.read_csv("TabeleTreningowe/Rezultaty Silhouette.csv", header=0, index_col=None)
        elif self.czyDaviesBouldin:
            rezultatyBF = pd.read_csv("TabeleTreningowe/Rezultaty DaviesBoudlin.csv", header=0, index_col=None)
        elif self.czyCalinskiHarabasz:
            rezultatyBF = pd.read_csv("TabeleTreningowe/Rezultaty CelinskiHarabasz.csv", header=0, index_col=None)
        rezultatyBF = rezultatyBF.round(4)
        self.tabelaBazowa = rezultatyBF

    def pokazTabele(self):
        try:
            model = PandasModel(self.tabelaBazowa)
            return model
        except Exception as inst:
            self.showDialog(inst)

    def testGreadSearchCV(self):

        if self.ui.comboBoxKlasyfikatory.currentIndex()==0:
            X = self.tabelaBazowa[self.tabelaBazowa.columns[0:48]].copy()
            y = self.tabelaBazowa[self.tabelaBazowa.columns[48]].copy()

            for index, row in y.iteritems():
                if row in 'DBScan euclidean':
                    y[index] = 11
                elif row in 'DBScan cityblock':
                    y[index] = 12
                elif row in 'DBScan cosine':
                    y[index] = 13
                elif row in 'KMeans euclidean':
                    y[index] = 21
                elif row in 'KMeans cityblock':
                    y[index] = 22
                elif row in 'KMeans cosine':
                    y[index] = 23
                elif row in 'Agglomerative euclidean':
                    y[index] = 31
                elif row in 'Agglomerative cityblock':
                    y[index] = 32
                elif row in 'Agglomerative cosine':
                    y[index] = 33

            y = y.astype(int)

            mlp = DecisionTreeClassifier()
            my_cv = LeaveOneOut()

            parametr_space = {}

            if self.czySilhouette:
                if self.ui.checkBoxCriterion.isChecked():
                    parametr_space.update({'criterion': [self.ui.lineEditCriterion_2.text().split(',')][0]})
                else:
                    parametr_space.update({'criterion': [self.konfiguracja.loc['Silhouette_klasyfikacja', 'criterion']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'max_depth': np.arange(self.ui.spinBoxMaxDepthOd.value(), self.ui.spinBoxMaxDepthDo.value(), self.ui.spinBoxMaxDepthCo.value())})
                else:
                    parametr_space.update({'max_depth': [self.konfiguracja.loc['Silhouette_klasyfikacja', 'max_depth']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'random_state': [self.ui.spinBoxRandomState_2.value()]})
                else:
                    parametr_space.update({'random_state': [self.konfiguracja.loc['Silhouette_klasyfikacja', 'random_state']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'min_samples_leaf': np.arange(self.ui.spinBoxMinSamplesLeafOd.value(), self.ui.spinBoxMinSamplesLeafDo.value(), self.ui.spinBoxMinSaplesLeafCo.value())})
                else:
                    parametr_space.update({'min_samples_leaf': [self.konfiguracja.loc['Silhouette_klasyfikacja', 'min_samples_leaf']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'min_samples_split': np.arange(self.ui.spinBoxMinSamplesSplitOd.value(), self.ui.spinBoxMinSaplesSplitDo.value(), self.ui.spinBoxMinSamplesSplitCo.value())})
                else:
                    parametr_space.update({'min_samples_split': [self.konfiguracja.loc['Silhouette_klasyfikacja', 'min_samples_split']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'splitter': [self.ui.lineEditSpliter_2.text().split(',')][0]})
                else:
                    parametr_space.update({'splitter': [self.konfiguracja.loc['Silhouette_klasyfikacja', 'splitter']]})
            elif self.czyDaviesBouldin:
                if self.ui.checkBoxCriterion.isChecked():
                    parametr_space.update({'criterion': [self.ui.lineEditCriterion_2.text().split(',')][0]})
                else:
                    parametr_space.update({'criterion': [self.konfiguracja.loc['DaviesBouldin_klasyfikacja', 'criterion']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'max_depth': np.arange(self.ui.spinBoxMaxDepthOd.value(),
                                                              self.ui.spinBoxMaxDepthDo.value(),
                                                              self.ui.spinBoxMaxDepthCo.value())})
                else:
                    parametr_space.update({'max_depth': [self.konfiguracja.loc['DaviesBouldin_klasyfikacja', 'max_depth']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'random_state': [self.ui.spinBoxRandomState_2.value()]})
                else:
                    parametr_space.update(
                        {'random_state': [self.konfiguracja.loc['DaviesBouldin_klasyfikacja', 'random_state']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'min_samples_leaf': np.arange(self.ui.spinBoxMinSamplesLeafOd.value(),
                                                                     self.ui.spinBoxMinSamplesLeafDo.value(),
                                                                     self.ui.spinBoxMinSaplesLeafCo.value())})
                else:
                    parametr_space.update(
                        {'min_samples_leaf': [self.konfiguracja.loc['DaviesBouldin_klasyfikacja', 'min_samples_leaf']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'min_samples_split': np.arange(self.ui.spinBoxMinSamplesSplitOd.value(),
                                                                      self.ui.spinBoxMinSaplesSplitDo.value(),
                                                                      self.ui.spinBoxMinSamplesSplitCo.value())})
                else:
                    parametr_space.update(
                        {'min_samples_split': [self.konfiguracja.loc['DaviesBouldin_klasyfikacja', 'min_samples_split']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'splitter': [self.ui.lineEditSpliter_2.text().split(',')][0]})
                else:
                    parametr_space.update({'splitter': [self.konfiguracja.loc['DaviesBouldin_klasyfikacja', 'splitter']]})

            elif self.czyCalinskiHarabasz:
                if self.ui.checkBoxCriterion.isChecked():
                    parametr_space.update({'criterion': [self.ui.lineEditCriterion_2.text().split(',')][0]})
                else:
                    parametr_space.update({'criterion': [self.konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'criterion']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'max_depth': np.arange(self.ui.spinBoxMaxDepthOd.value(),
                                                              self.ui.spinBoxMaxDepthDo.value(),
                                                              self.ui.spinBoxMaxDepthCo.value())})
                else:
                    parametr_space.update({'max_depth': [self.konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'max_depth']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'random_state': [self.ui.spinBoxRandomState_2.value()]})
                else:
                    parametr_space.update(
                        {'random_state': [self.konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'random_state']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'min_samples_leaf': np.arange(self.ui.spinBoxMinSamplesLeafOd.value(),
                                                                     self.ui.spinBoxMinSamplesLeafDo.value(),
                                                                     self.ui.spinBoxMinSaplesLeafCo.value())})
                else:
                    parametr_space.update(
                        {'min_samples_leaf': [self.konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'min_samples_leaf']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'min_samples_split': np.arange(self.ui.spinBoxMinSamplesSplitOd.value(),
                                                                      self.ui.spinBoxMinSaplesSplitDo.value(),
                                                                      self.ui.spinBoxMinSamplesSplitCo.value())})
                else:
                    parametr_space.update(
                        {'min_samples_split': [self.konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'min_samples_split']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'splitter': [self.ui.lineEditSpliter_2.text().split(',')][0]})
                else:
                    parametr_space.update({'splitter': [self.konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'splitter']]})


            clf = GridSearchCV(mlp, parametr_space, n_jobs=-1, cv=my_cv, verbose=3)
            clf.fit(X, y,)
            print('Najlepsze parametry:\n', clf.best_params_)

        elif self.ui.comboBoxKlasyfikatory.currentIndex()==1:
            X = self.tabelaBazowa[self.tabelaBazowa.columns[0:49]].copy()
            y = self.tabelaBazowa[self.tabelaBazowa.columns[49]].copy()

            temp = X[X.columns[-1]].copy()

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

            X['Metoda_metryka'] = temp.copy()
            y = y.astype(int)

            mlp = DecisionTreeRegressor()
            my_cv = LeaveOneOut()

            parametr_space = {}

            if self.czySilhouette:
                if self.ui.checkBoxCriterion.isChecked():
                    parametr_space.update({'criterion': [self.ui.lineEditCriterion_2.text().split(',')][0]})
                else:
                    parametr_space.update({'criterion': [self.konfiguracja.loc['Silhouette_regresja', 'criterion']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'max_depth': np.arange(self.ui.spinBoxMaxDepthOd.value(),
                                                              self.ui.spinBoxMaxDepthDo.value(),
                                                              self.ui.spinBoxMaxDepthCo.value())})
                else:
                    parametr_space.update({'max_depth': [self.konfiguracja.loc['Silhouette_regresja', 'max_depth']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'random_state': [self.ui.spinBoxRandomState_2.value()]})
                else:
                    parametr_space.update(
                        {'random_state': [self.konfiguracja.loc['Silhouette_regresja', 'random_state']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'min_samples_leaf': np.arange(self.ui.spinBoxMinSamplesLeafOd.value(),
                                                                     self.ui.spinBoxMinSamplesLeafDo.value(),
                                                                     self.ui.spinBoxMinSaplesLeafCo.value())})
                else:
                    parametr_space.update(
                        {'min_samples_leaf': [self.konfiguracja.loc['Silhouette_regresja', 'min_samples_leaf']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'min_samples_split': np.arange(self.ui.spinBoxMinSamplesSplitOd.value(),
                                                                      self.ui.spinBoxMinSaplesSplitDo.value(),
                                                                      self.ui.spinBoxMinSamplesSplitCo.value())})
                else:
                    parametr_space.update(
                        {'min_samples_split': [self.konfiguracja.loc['Silhouette_regresja', 'min_samples_split']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'splitter': [self.ui.lineEditSpliter_2.text().split(',')][0]})
                else:
                    parametr_space.update({'splitter': [self.konfiguracja.loc['Silhouette_regresja', 'splitter']]})

            elif self.czyDaviesBouldin:
                if self.ui.checkBoxCriterion.isChecked():
                    parametr_space.update({'criterion': [self.ui.lineEditCriterion_2.text().split(',')][0]})
                else:
                    parametr_space.update(
                        {'criterion': [self.konfiguracja.loc['DaviesBouldin_regresja', 'criterion']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'max_depth': np.arange(self.ui.spinBoxMaxDepthOd.value(),
                                                              self.ui.spinBoxMaxDepthDo.value(),
                                                              self.ui.spinBoxMaxDepthCo.value())})
                else:
                    parametr_space.update(
                        {'max_depth': [self.konfiguracja.loc['DaviesBouldin_regresja', 'max_depth']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'random_state': [self.ui.spinBoxRandomState_2.value()]})
                else:
                    parametr_space.update(
                        {'random_state': [self.konfiguracja.loc['DaviesBouldin_regresja', 'random_state']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'min_samples_leaf': np.arange(self.ui.spinBoxMinSamplesLeafOd.value(),
                                                                     self.ui.spinBoxMinSamplesLeafDo.value(),
                                                                     self.ui.spinBoxMinSaplesLeafCo.value())})
                else:
                    parametr_space.update(
                        {'min_samples_leaf': [self.konfiguracja.loc['DaviesBouldin_regresja', 'min_samples_leaf']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'min_samples_split': np.arange(self.ui.spinBoxMinSamplesSplitOd.value(),
                                                                      self.ui.spinBoxMinSaplesSplitDo.value(),
                                                                      self.ui.spinBoxMinSamplesSplitCo.value())})
                else:
                    parametr_space.update(
                        {'min_samples_split': [self.konfiguracja.loc['DaviesBouldin_regresja', 'min_samples_split']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'splitter': [self.ui.lineEditSpliter_2.text().split(',')][0]})
                else:
                    parametr_space.update({'splitter': [self.konfiguracja.loc['DaviesBouldin_regresja', 'splitter']]})

            elif self.czyCalinskiHarabasz:
                if self.ui.checkBoxCriterion.isChecked():
                    parametr_space.update({'criterion': [self.ui.lineEditCriterion_2.text().split(',')][0]})
                else:
                    parametr_space.update(
                        {'criterion': [self.konfiguracja.loc['CalinskiHarabasz_regresja', 'criterion']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'max_depth': np.arange(self.ui.spinBoxMaxDepthOd.value(),
                                                              self.ui.spinBoxMaxDepthDo.value(),
                                                              self.ui.spinBoxMaxDepthCo.value())})
                else:
                    parametr_space.update(
                        {'max_depth': [self.konfiguracja.loc['CalinskiHarabasz_regresja', 'max_depth']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'random_state': [self.ui.spinBoxRandomState_2.value()]})
                else:
                    parametr_space.update(
                        {'random_state': [self.konfiguracja.loc['CalinskiHarabasz_regresja', 'random_state']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'min_samples_leaf': np.arange(self.ui.spinBoxMinSamplesLeafOd.value(),
                                                                     self.ui.spinBoxMinSamplesLeafDo.value(),
                                                                     self.ui.spinBoxMinSaplesLeafCo.value())})
                else:
                    parametr_space.update(
                        {'min_samples_leaf': [self.konfiguracja.loc[
                            'CalinskiHarabasz_regresja', 'min_samples_leaf']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'min_samples_split': np.arange(self.ui.spinBoxMinSamplesSplitOd.value(),
                                                                      self.ui.spinBoxMinSaplesSplitDo.value(),
                                                                      self.ui.spinBoxMinSamplesSplitCo.value())})
                else:
                    parametr_space.update(
                        {'min_samples_split': [self.konfiguracja.loc[
                            'CalinskiHarabasz_regresja', 'min_samples_split']]})

                if self.ui.checkBoxMaxDepth.isChecked():
                    parametr_space.update({'splitter': [self.ui.lineEditSpliter_2.text().split(',')][0]})
                else:
                    parametr_space.update(
                        {'splitter': [self.konfiguracja.loc['CalinskiHarabasz_regresja', 'splitter']]})

            clf = GridSearchCV(mlp, parametr_space, n_jobs=-1, cv=my_cv, verbose=3, scoring='max_error')
            clf.fit(X, y)
            print('Najlepsze parametry:\n', clf.best_params_)




        # mlp = MLPClassifier(alpha=0.01, random_state=0,  learning_rate='constant', activation='tanh')
        # my_cv = LeaveOneOut()
        #
        # parameter_space = {
        #     'hidden_layer_sizes' : [(50,50,50),(100,100,100),(150,150,150),(100,150,100), (50,50),(100,100),(150,150),(200,200),
        #                             100, 200,250,300,350,500,800,1200],
        #     'solver': ['lbfgs', 'sgd'],
        #     'max_iter' : range(500, 5000, 500)
        # }

        # mlp = KNeighborsClassifier()
        # my_cv = LeaveOneOut()
        #
        # parameter_space = {
        #         'n_neighbors' : range(2,20,1),
        #         'weights' : ['uniform', 'distance'],
        #         'algorithm': ['auto', 'ball_tree', 'kd_tree','brute'],
        #         'leaf_size' : range(10,100, 10)
        #     }

        # mlp = KNeighborsRegressor()
        # my_cv = LeaveOneOut()
        #
        # parameter_space = {
        #         'n_neighbors' : range(2,20,1),
        #         'weights' : ['uniform', 'distance'],
        #         'algorithm': ['auto', 'ball_tree', 'kd_tree','brute'],
        #         'leaf_size' : range(10,60, 10)
        #     }

        #, scoring='max_error'









