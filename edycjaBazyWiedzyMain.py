
import sys

from PySide2.QtWidgets import QWidget, QMessageBox, QApplication
import pandas as pd

from PySide2.QtGui import QTextCursor
from Funkcje.SzukanieMetodDlaMiar.searchingBestMethodCelinskiHarabasz import szukanieCH
from Funkcje.SzukanieMetodDlaMiar.searchingBestMethodDaviesBoudlin import szukanieDaviesBoudlin
from Funkcje.SzukanieMetodDlaMiar.searchingBestMethodSilhouette import szukanieSilhouette
from Klasy.PandasModel import PandasModel
from forms.edycjaBazyWiedzy import Ui_edycjaBazyWiedzy

import os

class MyStdout:
    def __init__(self, buffer):
        self.buffer = buffer

    def write(self, string):
        if string:
            if 'Test ilosci klastrow' in string or 'Liczenie eps' in string:

                self.buffer.moveCursor(QTextCursor.End, QTextCursor.MoveAnchor)
                self.buffer.moveCursor(QTextCursor.StartOfLine, QTextCursor.MoveAnchor)
                self.buffer.moveCursor(QTextCursor.End, QTextCursor.KeepAnchor)
                storeCursorPos = self.buffer.textCursor()
                self.buffer.textCursor().removeSelectedText()
                self.buffer.textCursor().deletePreviousChar()
                self.buffer.setTextCursor(storeCursorPos)
                self.buffer.insertPlainText(string)
                self.buffer.moveCursor(QTextCursor.End, QTextCursor.MoveAnchor)
            else:
                self.buffer.append(string)
                self.buffer.moveCursor(QTextCursor.End, QTextCursor.MoveAnchor)
            QApplication.processEvents()


class EdycjaBazyWiedzy(QWidget):

    dane = pd.DataFrame()
    cechy = {}
    czySilhouette = False
    czyDaviesBouldin = False
    czyCalinskiHarabasz = False
    rezultatyBF = None

    wynikDoDodania = {}
    wynikBF = {}

    def __init__(self, dane, cechy, czySilhouette, czyDaviesBouldin, czyCalinskiHarabasz, wynikBF):
        super(EdycjaBazyWiedzy, self).__init__()
        self.ui = Ui_edycjaBazyWiedzy()
        self.ui.setupUi(self)
        self.show()
        self.dane = dane
        self.cechy = cechy
        self.czySilhouette = czySilhouette
        self.czyCalinskiHarabasz = czyCalinskiHarabasz
        self.czyDaviesBouldin = czyDaviesBouldin
        self.wynikBF = wynikBF

        self.wynikDoDodania.update(cechy)

        if len(self.wynikBF) > 0:
            self.wynikDoDodania.update(self.wynikBF)
            self.ui.textWynikiMonteCarlo.append("Test był przeprowadzony w poprzednim oknie")
            self.ui.textWynikiMonteCarlo.append(
                'Gotowy wpis do dodania:')
            self.ui.textWynikiMonteCarlo.append(str(self.wynikDoDodania))

        self.ui.tableViewTabelaNauki.setModel(self.pokazTabele())
        self.ui.tableViewTabelaNauki.horizontalHeader().setCascadingSectionResizes(True)
        self.ui.tableViewTabelaNauki.verticalHeader().setVisible(True)
        self.ui.tableViewTabelaNauki.verticalHeader().setCascadingSectionResizes(True)
        self.ui.tableViewTabelaNauki.resizeColumnsToContents()
        self.ui.btnZapiszPlik.clicked.connect(lambda: self.zapiszTabele())
        self.ui.btnUsunWiersz.clicked.connect(lambda: self.usunWiersz())
        self.ui.btnTestuj.clicked.connect(lambda: self.szukanieBruteForce())
        self.ui.btnDodajDoBazy.clicked.connect(lambda: self.dodajDoBazy())

        sys.stdout = MyStdout(self.ui.textWynikiMonteCarlo)
        sys.stderr = MyStdout(self.ui.textWynikiMonteCarlo)






    def pokazTabele(self):
        try:
            rezultatyBF = pd.DataFrame()
            if self.czySilhouette:
                rezultatyBF = pd.read_csv("TabeleTreningowe/Rezultaty Silhouette.csv", header=0, index_col=None)
            elif self.czyDaviesBouldin:
                rezultatyBF = pd.read_csv("TabeleTreningowe/Rezultaty DaviesBoudlin.csv", header=0, index_col=None)
            elif self.czyCalinskiHarabasz:
                rezultatyBF = pd.read_csv("TabeleTreningowe/Rezultaty CelinskiHarabasz.csv", header=0, index_col=None)
            rezultatyBF = rezultatyBF.round(4)
            self.rezultatyBF = rezultatyBF
            model = PandasModel(self.rezultatyBF)

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

    def usunWiersz(self):
        try:
            if self.dane.empty:
                self.showDialog('Dane nie zostały wczytane')
                return
            self.rezultatyBF = self.rezultatyBF.drop(self.ui.spinBoxUsuwanieIndeksu.value())
            model = PandasModel(self.rezultatyBF)
            self.ui.tableViewTabelaNauki.setModel(model)
        except Exception as inst:
            self.showDialog(inst)

    def zapiszTabele(self):
        if self.czySilhouette:
            self.rezultatyBF.to_csv("TabeleTreningowe/Rezultaty Silhouette.csv", index=False, header=True)
        elif self.czyDaviesBouldin:
            self.rezultatyBF.to_csv("TabeleTreningowe/Rezultaty DaviesBoudlin.csv", index=False, header=True)
        elif self.czyCalinskiHarabasz:
            self.rezultatyBF.to_csv("TabeleTreningowe/Rezultaty CelinskiHarabasz.csv", index=False, header=True)

    def szukanieBruteForce(self):
        if len(self.wynikBF) == 0:
            try:
                if self.dane.empty:
                    self.showDialog('Dane nie zostały wczytane')
                    return
                self.ui.textWynikiMonteCarlo.append(
                    'Rozpoczecie testu brute force dla zbioru.')
                QApplication.processEvents()
                if self.czySilhouette:
                    wynik = szukanieSilhouette(self.dane, self.dane, self.ui.spinBoxMaxIterMC.value(), self.ui.spinBoxIleKlastrowMC.value())
                elif self.czyDaviesBouldin:
                    wynik = szukanieDaviesBoudlin(self.dane, self.dane, self.ui.spinBoxMaxIterMC.value(), self.ui.spinBoxIleKlastrowMC.value())
                elif self.czyCalinskiHarabasz:
                    wynik = szukanieCH(self.dane, self.dane, self.ui.spinBoxMaxIterMC.value(), self.ui.spinBoxIleKlastrowMC.value())
                metoda = wynik.get('Metoda')
                metryka = wynik.get('Metryka')
                parametr = wynik.get('eps/k')
                if self.czySilhouette:
                    score = wynik.get('Wynik Silhouette')
                    score = round(score, 4)
                elif self.czyDaviesBouldin:
                    score = wynik.get('Wynik DaviesBoudlin')
                    score = round(score, 4)
                elif self.czyCalinskiHarabasz:
                    score = wynik.get('Wynik CelinskiHarabasz')
                    score = round(score, 2)

                self.ui.textWynikiMonteCarlo.append(' ')
                self.ui.textWynikiMonteCarlo.append(
                    'Znaleziona konfiguracja: ' + str(metoda) + " " + str(metryka) + " z parametrem " + str(parametr))
                self.ui.textWynikiMonteCarlo.append(
                    'Wynik miary: ' + str(score))
                QApplication.processEvents()

                self.wynikBF = {"Metoda_metryka": metoda + ' ' + metryka,
                                "Parametr": parametr,
                                "Wynik miary": score}

                self.wynikDoDodania.update(self.wynikBF)

                self.ui.textWynikiMonteCarlo.append(' ')

                self.ui.textWynikiMonteCarlo.append(
                    'Gotowy wpis do dodania:')
                self.ui.textWynikiMonteCarlo.append(str(self.wynikDoDodania))
                self.ui.textWynikiMonteCarlo.moveCursor(QTextCursor.End, QTextCursor.MoveAnchor)

                if self.ui.checkBoxWylaczPoTescie.isChecked():
                    self.wylaczenieKomputera()


            except Exception as inst:
                self.showDialog(inst)



    def dodajDoBazy(self):
        self.rezultatyBF = self.rezultatyBF.append(self.wynikDoDodania, ignore_index=True)
        self.rezultatyBF = self.rezultatyBF.round(4)
        model = PandasModel(self.rezultatyBF)
        self.ui.tableViewTabelaNauki.setModel(model)


    def wylaczenieKomputera(self):
        self.dodajDoBazy()
        self.zapiszTabele()
        os.system("shutdown /s /t 5")
        sys.exit()
