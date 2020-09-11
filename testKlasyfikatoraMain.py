from PySide2 import QtWidgets
from PySide2.QtWidgets import QWidget, QMessageBox, QApplication
import pandas as pd
from sklearn.model_selection import LeaveOneOut
from statistics import mean
from Klasy.PandasModel import PandasModel
from forms.testKlasyfikatora import Ui_TestKlasyfikatoraForm
from Funkcje.Klasyfikator.nauka import naukaTestMetodaMetryka, naukaTestParametr
import numpy as np

from konfiguracjaKlasyfikatoraMain import KonfiguracjaKlasyfikatora


class TestKlasyfikatora(QWidget):

    tabelaBazowa = None
    klasyfikatorMetodaMetryka = None
    klasyfikatorParametr = None

    def __init__(self, klasyfikatorMetodaMetryka, klasyfikatorParametr, czySilhouette, czyDaviesBouldin, czyCalinskiHarabasz):
        super(TestKlasyfikatora, self).__init__()
        self.ui = Ui_TestKlasyfikatoraForm()
        self.ui.setupUi(self)
        self.show()
        self.czySilhouette = czySilhouette
        self.czyCalinskiHarabasz = czyCalinskiHarabasz
        self.czyDaviesBouldin = czyDaviesBouldin

        klasyfikatory = ["Klasyfikator metody i metryki", "Klasyfikator parametru"]
        self.ui.comboBoxKlasyfikatory.addItems(klasyfikatory)
        self.ui.comboBoxKlasyfikatory.setCurrentIndex(0)
        self.ui.btnPokazTabele.clicked.connect(lambda: self.pokazTabele())
        self.ui.btnTestuj.clicked.connect(lambda: self.testLeaveOut())
        self.ui.btnZmienUstawieniaKlasyfikatora.clicked.connect(lambda : self.konfiguracjaKlasyfikatora())
        self.wczytajTabele()



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

    def showDialog(self, informacja):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(str(informacja))
        msgBox.setWindowTitle("Błąd")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    def zapiszWyniki(self):
        pass

    def testLeaveOut(self):
        if self.ui.comboBoxKlasyfikatory.currentIndex() == 0:
            X = self.tabelaBazowa[self.tabelaBazowa.columns[0:48]].copy()
            y = self.tabelaBazowa[self.tabelaBazowa.columns[48]].copy()
            self.ui.txtWyniki.clear()
            lou = LeaveOneOut()
            self.ui.txtWyniki.append(str(lou.get_n_splits(X)))
            QApplication.processEvents()
            listaWynikow = []
            for train_index, test_index in lou.split(X):
                self.ui.txtWyniki.append("TRAIN: " + str(train_index))
                self.ui.txtWyniki.append("TEST: " + str(test_index))
                QApplication.processEvents()
                X_train, X_test = X.loc[train_index], X.loc[test_index]
                y_train, y_test = y.loc[train_index], y.loc[test_index]
                klasyfikatorMetodaMetryka = naukaTestMetodaMetryka(X_train,y_train,self.czySilhouette, self.czyDaviesBouldin, self.czyCalinskiHarabasz)
                predykcja = klasyfikatorMetodaMetryka.predict(X_test)
                if predykcja == 11:
                    predykcja = 'DBScan euclidean'
                elif predykcja == 12:
                    predykcja = 'DBScan cityblock'
                elif predykcja == 13:
                    predykcja = 'DBScan cosine'
                elif predykcja == 21:
                    predykcja = 'KMeans euclidean'
                elif predykcja == 22:
                    predykcja = 'KMeans cityblock'
                elif predykcja == 23:
                    predykcja = 'KMeans cosine'
                elif predykcja == 31:
                    predykcja =  'Agglomerative euclidean'
                elif predykcja == 32:
                    predykcja = 'Agglomerative cityblock'
                elif predykcja == 33:
                    predykcja =  'Agglomerative cosine'

                if y_test.iloc[0] == predykcja:
                    listaWynikow.append("Trafione:")
                else:
                    listaWynikow.append("Nietrafione:")
                self.ui.txtWyniki.append("Miało być: " + str(y_test.iloc[0]))
                self.ui.txtWyniki.append("Przewidziano: " + str(predykcja))
                self.ui.txtWyniki.append(" ")
                QApplication.processEvents()
            wyniki = pd.Series(listaWynikow)
            self.ui.txtWyniki.append("Liczba wyników: ")
            self.ui.txtWyniki.append(str(wyniki.value_counts()))



        elif self.ui.comboBoxKlasyfikatory.currentIndex() == 1:
            X = self.tabelaBazowa[self.tabelaBazowa.columns[0:49]].copy()
            y = self.tabelaBazowa[self.tabelaBazowa.columns[49]].copy()

            self.ui.txtWyniki.clear()
            lou = LeaveOneOut()
            self.ui.txtWyniki.append(str(lou.get_n_splits(X)))
            QApplication.processEvents()
            listaWynikow = []
            for train_index, test_index in lou.split(X):
                self.ui.txtWyniki.append("TRAIN: " + str(train_index))
                self.ui.txtWyniki.append("TEST: " + str(test_index))
                QApplication.processEvents()
                X_train, X_test = X.loc[train_index], X.loc[test_index]
                y_train, y_test = y.loc[train_index], y.loc[test_index]
                klasyfikatorMetodaMetryka = naukaTestParametr(X_train, y_train, self.czySilhouette, self.czyDaviesBouldin, self.czyCalinskiHarabasz)


                if X_test.iloc[0,-1] in 'DBScan euclidean':
                    X_test.iat[0,-1] = 11
                elif X_test.iloc[0,-1] in 'DBScan cityblock':
                    X_test.iat[0,-1] = 12
                elif X_test.iloc[0,-1] in 'DBScan cosine':
                    X_test.iat[0,-1] = 13
                elif X_test.iloc[0,-1] in 'KMeans euclidean':
                    X_test.iat[0,-1] = 21
                elif X_test.iloc[0,-1] in 'KMeans cityblock':
                    X_test.iat[0,-1] = 22
                elif X_test.iloc[0,-1] in 'KMeans cosine':
                    X_test.iat[0,-1] = 23
                elif X_test.iloc[0,-1] in 'Agglomerative euclidean':
                    X_test.iat[0,-1] = 31
                elif X_test.iloc[0,-1] in 'Agglomerative cityblock':
                    X_test.iat[0,-1] = 32
                elif X_test.iloc[0,-1] in 'Agglomerative cosine':
                    X_test.iat[0,-1] = 33

                predykcja = klasyfikatorMetodaMetryka.predict(X_test)
                predykcja = predykcja.round()
                wynikProcentowy = round((np.fabs(y_test.iloc[0]-predykcja[0])/24) * 100, 2)

                if X_test[X_test.columns[48]].item() == 11:
                    pass
                else:
                    listaWynikow.append(wynikProcentowy)
                self.ui.txtWyniki.append("Miało być: " + str(y_test.iloc[0]))
                self.ui.txtWyniki.append("Przewidziano: " + str(predykcja[0]))
                self.ui.txtWyniki.append("Wynik procentowy: " + str(wynikProcentowy) + "%")
                self.ui.txtWyniki.append(" ")
                QApplication.processEvents()
            srednia = mean(listaWynikow)
            self.ui.txtWyniki.append("Średni poprawność klasyfikacji: " + str(round(srednia,2)))

    def konfiguracjaKlasyfikatora(self):
        try:

            window = QtWidgets.QWidget()
            konfiguracja = KonfiguracjaKlasyfikatora()

            return window
        except Exception as inst:
            self.showDialog(inst)