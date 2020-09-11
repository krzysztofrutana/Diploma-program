import os
import sys
import numpy as np
from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from numpy import unique, float64
from sklearn import preprocessing
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score

from Funkcje.Klasyfikator.nauka import nauka
from Funkcje.PomocniczeDlaMetod.DBSCAN_KNN import DB_SCAN
from Funkcje.SzukanieMetodDlaMiar.searchingBestMethodCelinskiHarabasz import szukanieCH
from Funkcje.SzukanieMetodDlaMiar.searchingBestMethodDaviesBoudlin import szukanieDaviesBoudlin
from Funkcje.SzukanieMetodDlaMiar.searchingBestMethodSilhouette import szukanieSilhouette
from Funkcje.WczytywanieDanych.loadNormalFiles import loadNormalFilesWithoutHeader, loadNormalFilesWithHeader
from Funkcje.WczytywanieDanych.loadTabFiles import loadTabFiles
from Funkcje.liczCechy import liczCechy
from forms.GUI import Ui_MainWindow
import pandas as pd
from Funkcje.Klasyfikator.klasyfikator import klasyfikacja
from sklearn.cluster import DBSCAN, AgglomerativeClustering
from Funkcje.PomocniczeDlaMetod.kmeans_with_metric import kmeans
from Klasy.PandasModel import PandasModel
from Klasy.PodgladTabel import PodgladDanych
from Klasy.terminalInTextEditors import MyStdoutTextEdit, MyStdoutLineText
from edycjaBazyWiedzyMain import EdycjaBazyWiedzy
from konfiguracjaKlasyfikatoraMain import KonfiguracjaKlasyfikatora
from testKlasyfikatoraMain import TestKlasyfikatora
from testParametrowMain import TestParametrow


class MainWindow(QMainWindow):

    dane = pd.DataFrame()
    cechy = {}

    proponowanaMetoda = ""
    proponowanaMetryka = ""
    wynikMiary = ""
    klasyfikatorMetodaMetryka = None
    klasyfikatorParametr = None
    wynikBF = {}


    def showDialog(self, informacja):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(str(informacja))
        msgBox.setWindowTitle("Błąd")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    def pokazDane(self):
        try:
            if self.dane.empty:
                self.showDialog('Dane nie zostały wczytane')
                return
            model = PandasModel(self.dane)
            dialog = PodgladDanych(model)
            dialog.exec_()
        except Exception as inst:
            self.showDialog(inst)

    def dbscan(self):
        try:
            dbscanKNN = DB_SCAN("Wariant" + str(self.dane))
            eps = dbscanKNN.KNNdist_plot(self.dane, 3, 'euclidean')
            if self.dane.empty:
                self.showDialog('Dane nie zostały wczytane')
                return
            daneDBScan = self.dane.copy()
            daneDBScan = daneDBScan.astype(float64)
            db = DBSCAN(eps=self.ui.doubleSpinBoxDBScanEps.value(), metric=self.ui.comboBoxDBScanMetryka.currentText()).fit(daneDBScan)
            core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
            core_samples_mask[db.core_sample_indices_] = True
            if len(unique(db.labels_)) > 1:
                if self.ui.radioButtonMiaraSilhouette.isChecked():
                    score_silhouette_DB = silhouette_score(self.dane, db.labels_, metric=self.ui.comboBoxDBScanMetryka.currentText())
                    score_silhouette_DB = round(score_silhouette_DB, 4)
                    self.ui.txtWynikSprawdzenia.setText(str(score_silhouette_DB))
                elif self.ui.radioButtonMiaraDaviesBoudlin.isChecked():
                    score_DaviesBoudlin_DB = davies_bouldin_score(self.dane, db.labels_)
                    score_DaviesBoudlin_DB = round(score_DaviesBoudlin_DB, 4)
                    self.ui.txtWynikSprawdzenia.setText(str(score_DaviesBoudlin_DB))
                elif self.ui.radioButtonMiaraCelinskiHarabasz.isChecked():
                    score_CalinskiHarabasz_DB = calinski_harabasz_score(self.dane, db.labels_)
                    score_CalinskiHarabasz_DB = round(score_CalinskiHarabasz_DB, 4)
                    self.ui.txtWynikSprawdzenia.setText(str(score_CalinskiHarabasz_DB))
        except Exception as inst:
            self.showDialog(inst)

    def kmeans(self):
        try:
            if self.dane.empty:
                self.showDialog('Dane nie zostały wczytane')
                return
            daneKMeans = self.dane.copy()
            daneKMeans = daneKMeans.astype(float64)
            if self.ui.comboBoxKMeansMetryka.currentText() in 'cosine':
                daneKMeans = preprocessing.normalize(daneKMeans, norm='l2')
            KM = kmeans(daneKMeans, n_clusters=self.ui.spinBoxKMeansIloscKlastrow.value(), metric=self.ui.comboBoxKMeansMetryka.currentText(), maxiter=1000, verbose=0)
            labelsKM = KM[1]
            if self.ui.radioButtonMiaraSilhouette.isChecked():
                score_silhouette_KM = silhouette_score(self.dane, labelsKM,
                                                       metric=self.ui.comboBoxKMeansMetryka.currentText())
                score_silhouette_KM = round(score_silhouette_KM, 4)
                self.ui.txtWynikSprawdzenia.setText(str(score_silhouette_KM))
            elif self.ui.radioButtonMiaraDaviesBoudlin.isChecked():
                score_DaviesBoudlin_KM = davies_bouldin_score(self.dane, labelsKM)
                score_DaviesBoudlin_KM = round(score_DaviesBoudlin_KM, 4)
                self.ui.txtWynikSprawdzenia.setText(str(score_DaviesBoudlin_KM))
            elif self.ui.radioButtonMiaraCelinskiHarabasz.isChecked():
                score_CalinskiHarabasz_KM = calinski_harabasz_score(self.dane, labelsKM)
                score_CalinskiHarabasz_KM = round(score_CalinskiHarabasz_KM, 4)
                self.ui.txtWynikSprawdzenia.setText(str(score_CalinskiHarabasz_KM))
        except Exception as inst:
            self.showDialog(inst)

    def agglomerative(self):
        try:
            if self.dane.empty:
                self.showDialog('Dane nie zostały wczytane')
                return
            daneAgglomerative = self.dane.copy()
            daneAgglomerative = daneAgglomerative.astype(float64)
            ac = AgglomerativeClustering(n_clusters=self.ui.spinBoxAgglomerativeIloscKlastrow.value(), affinity=self.ui.comboBoxAgglomerativeMetryka.currentText()
                                     , linkage="average").fit(daneAgglomerative)
            labelsAC = ac.labels_
            if self.ui.radioButtonMiaraSilhouette.isChecked():
                score_silhouette_AC = silhouette_score(self.dane, labelsAC,
                                                   metric=self.ui.comboBoxAgglomerativeMetryka.currentText())
                score_silhouette_AC = round(score_silhouette_AC, 4)
                self.ui.txtWynikSprawdzenia.setText(str(score_silhouette_AC))
            elif self.ui.radioButtonMiaraDaviesBoudlin.isChecked():
                score_DaviesBoudlin_AC = davies_bouldin_score(self.dane, labelsAC)
                score_DaviesBoudlin_AC = round(score_DaviesBoudlin_AC, 4)
                self.ui.txtWynikSprawdzenia.setText(str(score_DaviesBoudlin_AC))
            elif self.ui.radioButtonMiaraCelinskiHarabasz.isChecked():
                score_CalinskiHarabasz_AC = calinski_harabasz_score(self.dane, labelsAC)
                score_CalinskiHarabasz_AC = round(score_CalinskiHarabasz_AC, 4)
                self.ui.txtWynikSprawdzenia.setText(str(score_CalinskiHarabasz_AC))
        except Exception as inst:
            self.showDialog(inst)

    def pokazTabele(self):
        try:
            rezultatyBF = pd.DataFrame()
            if self.ui.radioButtonMiaraSilhouette.isChecked():
                rezultatyBF = pd.read_csv("TabeleTreningowe/Rezultaty Silhouette.csv")
            elif self.ui.radioButtonMiaraDaviesBoudlin.isChecked():
                rezultatyBF = pd.read_csv("TabeleTreningowe/Rezultaty DaviesBoudlin.csv")
            elif self.ui.radioButtonMiaraCelinskiHarabasz.isChecked():
                rezultatyBF = pd.read_csv("TabeleTreningowe/Rezultaty CelinskiHarabasz.csv")
            model = PandasModel(rezultatyBF)
            dialog = PodgladDanych(model)
            dialog.exec_()
        except Exception as inst:
            self.showDialog(inst)

    def openFileDialog(self):
        self.dialog = QFileDialog.getOpenFileName(self,
                                       "/home",
                                        )
        self.ui.lineEditSciezkaPliku.setText(str(self.dialog[0]))
        if '.tab' in str(self.dialog[0]):
            self.ui.radioButtonPlikTAB.setChecked(True)

    def wczytywaniePliku(self):
        try:
            sciezkaDoPliku = self.ui.lineEditSciezkaPliku.text()
            if len(sciezkaDoPliku)== 0:
                self.showDialog('Plik nie zostal wybrany')
                return
            if '.tab' in sciezkaDoPliku:
                self.ui.radioButtonPlikTAB.setChecked(True)
            if self.ui.radioButtonPlikTAB.isChecked():
                self.dane = loadTabFiles(sciezkaDoPliku)
            if self.ui.radioButtonCSVbezNaglowkow.isChecked():
                self.dane = loadNormalFilesWithoutHeader(sciezkaDoPliku, self.ui.txtJakiSeparator.text())
            if self.ui.radioButtonCSVzNaglowkami.isChecked():
                self.dane = loadNormalFilesWithHeader(sciezkaDoPliku, self.ui.txtJakiSeparator.text())
            if self.dane.shape[1]==1:
                self.showDialog('Dane niepoprawne, zawierają tylko jeden atrybut, wybierz inne dane')
                return
            else:
                self.statusBar().showMessage('Plik wczytany')
            self.ui.spinBoxIleKolumn.setValue(self.dane.shape[1])
            self.ui.spinBoxIleWierszy.setValue(self.dane.shape[0])
        except Exception as inst:
            self.showDialog(inst)

    def liczenieCech(self):
        self.statusBar().showMessage('Rozpoczęcie liczenia cech danych')
        try:
            if self.dane.empty:
                self.showDialog('Dane nie zostały wczytane')
                return
            sys.stdout = MyStdoutLineText(self.ui.lineEditPostep)
            sys.stderr = MyStdoutLineText(self.ui.lineEditPostep)
            cechy, self.dane = liczCechy(self.dane, self.ui.lineEditSciezkaPliku.text(), self.ui.checkBoxAtrybutDecyzyjny.isChecked(),
                                         self.ui.spinBoxIndexAtrybutu.value(), self.ui.checkBoxAtrybutIndeksujacy.isChecked(),
                                         (self.ui.spinBoxIndexIndeksujacy.value()-1))
            print(cechy)
            self.cechy = cechy
            self.pokazCechy()
            self.statusBar().showMessage('Liczenie cech zakończone pomyślnie', 2000)
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
        except Exception as inst:
            self.showDialog(inst)
            print(inst)
            pass

    def pokazCechy(self):
        if len(self.cechy) > 0:
            cechy = pd.DataFrame([self.cechy])
            naglowki = list(cechy.columns.values)
            naglowki = pd.DataFrame(naglowki, index=naglowki)
            daneVertical = pd.DataFrame(cechy)
            daneVertical = daneVertical.T
            daneVertical = daneVertical.round(3)
            daneVertical = pd.concat([naglowki[0], daneVertical[0]], axis=1)
            daneVertical = daneVertical.round(4)
            model = PandasModel(daneVertical)
            self.ui.tableViewCechyDanych.setModel(model)
            self.ui.tableViewCechyDanych.resizeColumnsToContents()

    def klasyfikuj(self):
        try:
            if self.dane.empty:
                self.showDialog('Dane nie zostały wczytane')
                return
            elif len(self.cechy) == 0:
                self.showDialog('Cechy nie zostały obliczone')
                return
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            if self.ui.radioButtonMiaraSilhouette.isChecked():
                metoda, metryka, propParametr, wynik= klasyfikacja(self.dane, self.cechy, self.klasyfikatorMetodaMetryka,
                                                                        self.klasyfikatorParametr, 'silhouette')
                wynik = round(wynik, 4)

                self.proponowanaMetoda = metoda
                self.proponowanaMetryka = metryka
                self.wynikMiary = wynik
                strMetodaMetrykaParametr = metoda + " " + metryka + " z parametrem "+ str(int(propParametr))
                self.ui.txtProponowanaMetoda.setText(strMetodaMetrykaParametr)
                self.ui.txtWynikProponowanaMetoda.setText(str(wynik))
                self.ui.txtWynikMetodaZKlasyfikacji.setText(str(wynik))

            if self.ui.radioButtonMiaraDaviesBoudlin.isChecked():
                metoda, metryka, propParametr,wynik = klasyfikacja(self.dane, self.cechy, self.klasyfikatorMetodaMetryka,
                                                                        self.klasyfikatorParametr,  'daviesBoudlin')
                wynik = round(wynik, 4)

                self.proponowanaMetoda = metoda
                self.proponowanaMetryka = metryka
                self.wynikMiary = wynik
                strMetodaMetrykaParametr = metoda + " " + metryka + " z parametrem "+ str(int(propParametr))
                self.ui.txtProponowanaMetoda.setText(strMetodaMetrykaParametr)
                self.ui.txtWynikProponowanaMetoda.setText(str(wynik))
                self.ui.txtWynikMetodaZKlasyfikacji.setText(str(wynik))

            if self.ui.radioButtonMiaraCelinskiHarabasz.isChecked():
                metoda, metryka, propParametr,wynik = klasyfikacja(self.dane, self.cechy, self.klasyfikatorMetodaMetryka,
                                                                        self.klasyfikatorParametr, 'calinskiHarabasz')
                wynik = round(wynik, 2)

                self.proponowanaMetoda = metoda
                self.proponowanaMetryka = metryka
                self.wynikMiary = wynik
                strMetodaMetrykaParametr = metoda + " " + metryka + " z parametrem "+ str(int(propParametr))
                self.ui.txtProponowanaMetoda.setText(strMetodaMetrykaParametr)
                self.ui.txtWynikProponowanaMetoda.setText(str(wynik))
                self.ui.txtWynikMetodaZKlasyfikacji.setText(str(wynik))
                if len(self.ui.txtZnalezionaMetodaBF.text()) > 0:
                    bladKlasyfikacji = np.fabs(
                        float(self.ui.txtWynikZBruteForce.text()) - float(self.ui.txtWynikMetodaZKlasyfikacji.text()))
                    bladKlasyfikacji = round(bladKlasyfikacji, 3)
                    self.ui.txtBladKlasyfikacji.setText(str(bladKlasyfikacji))
            self.pokazCechy()
            self.statusBar().showMessage('Klasyfikacja pomyślna', 3000)
        except Exception as inst:
            self.showDialog(inst)

    def szukanieBruteForce(self):
        try:
            if self.dane.empty:
                self.showDialog('Dane nie zostały wczytane')
                return
            self.statusBar().showMessage(
                'Rozpoczęcie szukania optymalnej metody i metryki metodą Brute Force, proszę czekać')

            sys.stdout = MyStdoutTextEdit(self.ui.textEditBFGui)
            sys.stderr = MyStdoutTextEdit(self.ui.textEditBFGui)
            if self.ui.radioButtonMiaraSilhouette.isChecked():
                wynik = szukanieSilhouette(self.dane, self.dane, 1000, 25)
            elif self.ui.radioButtonMiaraDaviesBoudlin.isChecked():
                wynik = szukanieDaviesBoudlin(self.dane, self.dane, 1000, 25)
            elif self.ui.radioButtonMiaraCelinskiHarabasz.isChecked():
                wynik = szukanieCH(self.dane, self.dane, 1000, 25)
            metoda = wynik.get('Metoda')
            metryka = wynik.get('Metryka')
            parametr = wynik.get('eps/k')
            if self.ui.radioButtonMiaraSilhouette.isChecked():
                score = wynik.get('Wynik Silhouette')
                score = round(score, 4)
            elif self.ui.radioButtonMiaraDaviesBoudlin.isChecked():
                score = wynik.get('Wynik DaviesBoudlin')
                score = round(score, 4)
            elif self.ui.radioButtonMiaraCelinskiHarabasz.isChecked():
                score = wynik.get('Wynik CelinskiHarabasz')
                score = round(score, 2)
            strMetodaMetrykaParametr = metoda + " " + metryka + " z parametrem " + str(parametr)
            self.ui.txtZnalezionaMetodaBF.setText(strMetodaMetrykaParametr)
            self.ui.txtZnalezionyWynikBF.setText(str(score))
            self.ui.txtWynikZBruteForce.setText(str(score))

            self.wynikBF = {"Metoda_metryka":metoda + ' '+ metryka,
                            "Parametr": parametr,
                            "Wynik miary":score}

            if len(self.ui.txtWynikMetodaZKlasyfikacji.text())>0:
                bladKlasyfikacji = np.fabs(float(self.ui.txtWynikZBruteForce.text())-float(self.ui.txtWynikMetodaZKlasyfikacji.text()))
                bladKlasyfikacji = round(bladKlasyfikacji, 3)
                self.ui.txtBladKlasyfikacji.setText(str(bladKlasyfikacji))
            self.statusBar().showMessage('Szukanie optymalnej metody zakończone sukcesem', 3000)
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
        except Exception as inst:
            self.showDialog(inst)

    def usunKolumne(self):
        try:
            if self.dane.empty:
                self.showDialog('Dane nie zostały wczytane')
                return
            self.dane = self.dane.drop(columns=self.dane.columns[self.ui.spinBoxUsuwanieKolumny.value()])
        except Exception as inst:
            self.showDialog(inst)

    def podgladNotepad(self):
        try:
            osCommandString = "notepad.exe "+ self.ui.lineEditSciezkaPliku.text()
            os.system(osCommandString)
        except Exception as inst:
            self.showDialog(inst)

    def zmianaKlasyfikatora(self):
        try:
            if self.ui.radioButtonMiaraSilhouette.isChecked():
                self.klasyfikatorMetodaMetryka, self.klasyfikatorParametr = nauka('silhouette')

            elif self.ui.radioButtonMiaraDaviesBoudlin.isChecked():
                self.klasyfikatorMetodaMetryka, self.klasyfikatorParametr = nauka('daviesBoudlin')
            elif self.ui.radioButtonMiaraCelinskiHarabasz.isChecked():
                self.klasyfikatorMetodaMetryka, self.klasyfikatorParametr= nauka('calinskiHarabasz')

            self.ui.txtProponowanaMetoda.setText('')
            self.ui.txtWynikProponowanaMetoda.setText('')

            self.ui.txtZnalezionaMetodaBF.setText('')
            self.ui.txtZnalezionyWynikBF.setText('')
            self.ui.textEditBFGui.clear()

            self.ui.txtWynikMetodaZKlasyfikacji.setText('')
            self.ui.txtWynikZBruteForce.setText('')
            self.ui.txtBladKlasyfikacji.setText('')
            self.statusBar().showMessage('Zmiana/update klasyfikatora/metody pomyślna', 2000)

        except Exception as inst:
            self.showDialog(inst)

    def pokazWariancjeKolumn(self):
        try:
            if self.dane.empty:
                self.showDialog('Dane nie zostały wczytane')
                return
            wariancjaWKolumnach = []
            dane = self.dane.astype(float64)
            header = list(dane.columns.values)
            listy = []
            for i in range(0, dane.shape[1], 1):
                bufor = dane[dane.columns[i]]
                wariancja = bufor.var()
                wariancjaWKolumnach.append(wariancja)
            listy.append(header)
            listy.append(wariancjaWKolumnach)
            wariancjaWKolumnach = np.vstack(tuple(listy))
            wariancjaWKolumnachDF = pd.DataFrame(wariancjaWKolumnach[1:], columns=header)
            wariancjaWKolumnachDF = wariancjaWKolumnachDF.round(4)
            model = PandasModel(wariancjaWKolumnachDF)
            dialog = PodgladDanych(model)
            dialog.exec_()
        except Exception as inst:
            self.showDialog(inst)

    def pelneCzyszczenieGUI(self):
        try:
            self.ui.lineEditSciezkaPliku.setText('')
            self.ui.txtJakiSeparator.setText('')
            self.ui.spinBoxUsuwanieKolumny.setValue(0)
            self.ui.spinBoxIleWierszy.setValue(0)
            self.ui.spinBoxIleKolumn.setValue(0)
            self.ui.checkBoxAtrybutDecyzyjny.setChecked(False)
            self.ui.spinBoxIndexAtrybutu.setValue(0)
            self.ui.checkBoxAtrybutIndeksujacy.setChecked(False)
            self.ui.spinBoxIndexIndeksujacy.setValue(0)
            self.ui.lineEditPostep.setText('')


            self.ui.txtProponowanaMetoda.setText('')
            self.ui.txtWynikProponowanaMetoda.setText('')

            self.ui.txtZnalezionaMetodaBF.setText('')
            self.ui.txtZnalezionyWynikBF.setText('')
            self.ui.textEditBFGui.clear()

            self.ui.txtWynikMetodaZKlasyfikacji.setText('')
            self.ui.txtWynikZBruteForce.setText('')
            self.ui.txtBladKlasyfikacji.setText('')

            self.ui.doubleSpinBoxDBScanEps.setValue(0.00)
            self.ui.spinBoxKMeansIloscKlastrow.setValue(0)
            self.ui.spinBoxAgglomerativeIloscKlastrow.setValue(0)
            self.ui.comboBoxDBScanMetryka.setCurrentIndex(0)
            self.ui.comboBoxKMeansMetryka.setCurrentIndex(0)
            self.ui.comboBoxAgglomerativeMetryka.setCurrentIndex(0)

            self.ui.txtWynikSprawdzenia.setText('')

            self.dane = pd.DataFrame()
            self.cechy = {}
            cechy = pd.DataFrame([self.cechy])
            model = PandasModel(cechy)
            self.ui.tableViewCechyDanych.setModel(model)

            self.ui.tableViewCechyDanych.clearSpans()
            self.proponowanaMetoda = ""
            self.proponowanaMetryka = ""
            self.wynikMiary = ""
            self.wynikBF = {}
        except Exception as inst:
            print(inst)
            pass

    def edycjaBazyWiedzy(self):
        try:
            if self.dane.empty:
                self.showDialog('Dane nie zostały wczytane')
                return
            elif len(self.cechy) == 0:
                self.showDialog('Cechy nie zostały obliczone')
                return
            self.window = QtWidgets.QWidget()
            self.badania = EdycjaBazyWiedzy(self.dane, self.cechy, self.ui.radioButtonMiaraSilhouette.isChecked(), self.ui.radioButtonMiaraDaviesBoudlin.isChecked(),
                                self.ui.radioButtonMiaraCelinskiHarabasz.isChecked(), self.wynikBF)
            return window
        except Exception as inst:
            self.showDialog(inst)

    def testKlasyfikatora(self):
        try:
            self.window = QtWidgets.QWidget()
            self.badania = TestKlasyfikatora(self.klasyfikatorMetodaMetryka, self.klasyfikatorParametr, self.ui.radioButtonMiaraSilhouette.isChecked(), self.ui.radioButtonMiaraDaviesBoudlin.isChecked(),
                                self.ui.radioButtonMiaraCelinskiHarabasz.isChecked())
            return window
        except Exception as inst:
            self.showDialog(inst)

    def konfiguracjaKlasyfikatora(self):
        try:

            self.window = QtWidgets.QWidget()
            self.konfiguracja = KonfiguracjaKlasyfikatora()

            return window
        except Exception as inst:
            self.showDialog(inst)

    def testParametrow(self):
        try:

            self.window = QtWidgets.QWidget()
            self.badania = TestParametrow(self.ui.radioButtonMiaraSilhouette.isChecked(), self.ui.radioButtonMiaraDaviesBoudlin.isChecked(),
                                self.ui.radioButtonMiaraCelinskiHarabasz.isChecked())
            return window
        except Exception as inst:
            self.showDialog(inst)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        self.ui.btnWybierzPlik.clicked.connect(lambda: self.openFileDialog())

        self.ui.btnLiczCechy.clicked.connect(lambda: self.liczenieCech())

        self.ui.btnPodgladDanych.clicked.connect(lambda: self.pokazDane())
        self.ui.btnOtworzPlik.clicked.connect(lambda: self.wczytywaniePliku())
        self.ui.btnKlasyfikuj.clicked.connect(lambda: self.klasyfikuj())
        self.ui.btnSzukajBruteForce.clicked.connect(lambda: self.szukanieBruteForce())

        metryki = ['euclidean', 'cityblock', 'cosine']

        self.ui.comboBoxKMeansMetryka.addItems(metryki)
        self.ui.comboBoxKMeansMetryka.setCurrentIndex(0)
        self.ui.comboBoxAgglomerativeMetryka.addItems(metryki)
        self.ui.comboBoxAgglomerativeMetryka.setCurrentIndex(0)
        self.ui.comboBoxDBScanMetryka.addItems(metryki)
        self.ui.comboBoxDBScanMetryka.setCurrentIndex(0)
        self.ui.pushButtonKMeansSprawdz.clicked.connect(lambda: self.kmeans())
        self.ui.pushButtonAgglomerativeSprawdz.clicked.connect(lambda: self.agglomerative())
        self.ui.btnDBScanSprawdz.clicked.connect(lambda: self.dbscan())


        self.zmianaKlasyfikatora()
        self.ui.radioButtonMiaraSilhouette.toggled.connect(lambda: self.zmianaKlasyfikatora())
        self.ui.radioButtonMiaraDaviesBoudlin.toggled.connect(lambda: self.zmianaKlasyfikatora())
        self.ui.radioButtonMiaraCelinskiHarabasz.toggled.connect(lambda: self.zmianaKlasyfikatora())

        self.ui.actionPodgladTabeliTreningowej.triggered.connect(lambda: self.pokazTabele())
        self.ui.actionWariancja_kolumn.triggered.connect(lambda:  self.pokazWariancjeKolumn())
        self.ui.actionCzyszczenie.triggered.connect(lambda: self.pelneCzyszczenieGUI())
        self.ui.actionTest_Leave_Out_klasyfikatora.triggered.connect(lambda: self.testKlasyfikatora())
        self.ui.actionKonfiguracja_klasyfikatora.triggered.connect(lambda: self.konfiguracjaKlasyfikatora())

        self.ui.actionEdycja_bazy_wiedzy.triggered.connect(lambda: self.edycjaBazyWiedzy())
        self.ui.actionTest_parametr_w_klasyfikatora.triggered.connect(lambda: self.testParametrow())

        self.ui.btnUsunKolumne.clicked.connect(lambda: self.usunKolumne())

        self.ui.btnPodgladNotepad.clicked.connect(lambda: self.podgladNotepad())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

