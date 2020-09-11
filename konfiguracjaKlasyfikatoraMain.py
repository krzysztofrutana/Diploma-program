import PySide2
from PySide2.QtWidgets import QWidget
import pandas as pd
from forms.konfiguracjaKlasyfikatora import Ui_FormKonfiguracjaKlasyfikatora



class KonfiguracjaKlasyfikatora(QWidget):

    def __init__(self):
        super(KonfiguracjaKlasyfikatora, self).__init__()
        self.ui = Ui_FormKonfiguracjaKlasyfikatora()
        self.ui.setupUi(self)
        self.show()
        self.konfiguracja = pd.read_csv('Funkcje/Klasyfikator/properties.csv', header=0, index_col=0)

        klasyfikatory = ["Klasyfikator", "Klasyfikator regresyjny"]
        self.ui.comboBoxWyborKlasyfikatora.addItems(klasyfikatory)
        self.ui.comboBoxWyborKlasyfikatora.setCurrentIndex(0)

        miara = ["Silhouette", "Davies Bouldin", "Calinski Harabasz"]
        self.ui.comboBoxWyborMiar.addItems(miara)
        self.ui.comboBoxWyborMiar.setCurrentIndex(0)

        self.ui.pushButtonWczytajKonfiguracje.clicked.connect(lambda : self.pokazKonfiguracje())
        self.ui.btnZapisz.clicked.connect(lambda : self.zapiszKonfiguracje())



    def pokazKonfiguracje(self):
        if self.ui.comboBoxWyborKlasyfikatora.currentIndex() == 0:
            if self.ui.comboBoxWyborMiar.currentIndex() == 0:
                self.ui.lineEditCriterion.setText(self.konfiguracja.loc['Silhouette_klasyfikacja', 'criterion'])
                if self.konfiguracja.loc['Silhouette_klasyfikacja', 'max_depth'] == 'None':
                    self.ui.checkBoxMaxDepthNone.setChecked(True)
                else:
                    self.ui.spinBoxMaxDepth.setValue(self.konfiguracja.loc['Silhouette_klasyfikacja', 'max_depth'])
                self.ui.spinBoxRandomState.setValue(self.konfiguracja.loc['Silhouette_klasyfikacja', 'random_state'])
                self.ui.spinBoxMinSamplesLeaf.setValue(self.konfiguracja.loc['Silhouette_klasyfikacja', 'min_samples_leaf'])
                self.ui.spinBoxMinSamplesSplit.setValue(
                    self.konfiguracja.loc['Silhouette_klasyfikacja', 'min_samples_split'])
                self.ui.lineEditSpliter.setText(self.konfiguracja.loc['Silhouette_klasyfikacja', 'splitter'])
            elif self.ui.comboBoxWyborMiar.currentIndex() == 1:
                self.ui.lineEditCriterion.setText(self.konfiguracja.loc['DaviesBouldin_klasyfikacja', 'criterion'])
                if self.konfiguracja.loc['DaviesBouldin_klasyfikacja', 'max_depth'] == 'None':
                    self.ui.checkBoxMaxDepthNone.setChecked(True)
                else:
                    self.ui.spinBoxMaxDepth.setValue(self.konfiguracja.loc['DaviesBouldin_klasyfikacja', 'max_depth'])
                self.ui.spinBoxRandomState.setValue(self.konfiguracja.loc['DaviesBouldin_klasyfikacja', 'random_state'])
                self.ui.spinBoxMinSamplesLeaf.setValue(self.konfiguracja.loc['DaviesBouldin_klasyfikacja', 'min_samples_leaf'])
                self.ui.spinBoxMinSamplesSplit.setValue(
                    self.konfiguracja.loc['DaviesBouldin_klasyfikacja', 'min_samples_split'])
                self.ui.lineEditSpliter.setText(self.konfiguracja.loc['DaviesBouldin_klasyfikacja', 'splitter'])
            elif self.ui.comboBoxWyborMiar.currentIndex() == 2:
                self.ui.lineEditCriterion.setText(self.konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'criterion'])
                if self.konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'max_depth'] == 'None':
                    self.ui.checkBoxMaxDepthNone.setChecked(True)
                else:
                    self.ui.spinBoxMaxDepth.setValue(self.konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'max_depth'])
                self.ui.spinBoxRandomState.setValue(self.konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'random_state'])
                self.ui.spinBoxMinSamplesLeaf.setValue(self.konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'min_samples_leaf'])
                self.ui.spinBoxMinSamplesSplit.setValue(
                    self.konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'min_samples_split'])
                self.ui.lineEditSpliter.setText(self.konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'splitter'])
        elif self.ui.comboBoxWyborKlasyfikatora.currentIndex() == 1:
            if self.ui.comboBoxWyborMiar.currentIndex() == 0:
                self.ui.lineEditCriterion.setText(self.konfiguracja.loc['Silhouette_regresja', 'criterion'])
                if self.konfiguracja.loc['Silhouette_regresja', 'max_depth'] == 'None':
                    self.ui.checkBoxMaxDepthNone.setChecked(True)
                else:
                    self.ui.spinBoxMaxDepth.setValue(self.konfiguracja.loc['Silhouette_regresja', 'max_depth'])
                self.ui.spinBoxRandomState.setValue(self.konfiguracja.loc['Silhouette_regresja', 'random_state'])
                self.ui.spinBoxMinSamplesLeaf.setValue(self.konfiguracja.loc['Silhouette_regresja', 'min_samples_leaf'])
                self.ui.spinBoxMinSamplesSplit.setValue(
                    self.konfiguracja.loc['Silhouette_regresja', 'min_samples_split'])
                self.ui.lineEditSpliter.setText(self.konfiguracja.loc['Silhouette_regresja', 'splitter'])
            elif self.ui.comboBoxWyborMiar.currentIndex() == 1:
                self.ui.lineEditCriterion.setText(self.konfiguracja.loc['DaviesBouldin_regresja', 'criterion'])
                if self.konfiguracja.loc['DaviesBouldin_regresja', 'max_depth'] == 'None':
                    self.ui.checkBoxMaxDepthNone.setChecked(True)
                else:
                    self.ui.spinBoxMaxDepth.setValue(self.konfiguracja.loc['DaviesBouldin_regresja', 'max_depth'])
                self.ui.spinBoxRandomState.setValue(self.konfiguracja.loc['DaviesBouldin_regresja', 'random_state'])
                self.ui.spinBoxMinSamplesLeaf.setValue(self.konfiguracja.loc['DaviesBouldin_regresja', 'min_samples_leaf'])
                self.ui.spinBoxMinSamplesSplit.setValue(
                    self.konfiguracja.loc['DaviesBouldin_regresja', 'min_samples_split'])
                self.ui.lineEditSpliter.setText(self.konfiguracja.loc['DaviesBouldin_regresja', 'splitter'])
            elif self.ui.comboBoxWyborMiar.currentIndex() == 2:
                self.ui.lineEditCriterion.setText(self.konfiguracja.loc['CalinskiHarabasz_regresja', 'criterion'])
                if self.konfiguracja.loc['CalinskiHarabasz_regresja', 'max_depth'] == 'None':
                    self.ui.checkBoxMaxDepthNone.setChecked(True)
                else:
                    self.ui.spinBoxMaxDepth.setValue(self.konfiguracja.loc['CalinskiHarabasz_regresja', 'max_depth'])
                self.ui.spinBoxRandomState.setValue(self.konfiguracja.loc['CalinskiHarabasz_regresja', 'random_state'])
                self.ui.spinBoxMinSamplesLeaf.setValue(self.konfiguracja.loc['CalinskiHarabasz_regresja', 'min_samples_leaf'])
                self.ui.spinBoxMinSamplesSplit.setValue(
                    self.konfiguracja.loc['CalinskiHarabasz_regresja', 'min_samples_split'])
                self.ui.lineEditSpliter.setText(self.konfiguracja.loc['CalinskiHarabasz_regresja', 'splitter'])

    def zapiszKonfiguracje(self):
        if self.ui.comboBoxWyborKlasyfikatora.currentIndex() == 0:
            if self.ui.comboBoxWyborMiar.currentIndex() == 0:
                self.konfiguracja.loc['Silhouette_klasyfikacja', 'criterion'] = self.ui.lineEditCriterion.text()
                if self.ui.checkBoxMaxDepthNone.isChecked():
                    self.konfiguracja.loc['Silhouette_klasyfikacja', 'max_depth'] = 'None'
                else:
                    self.konfiguracja.loc['Silhouette_klasyfikacja', 'max_depth'] = int(self.ui.spinBoxMaxDepth.value())
                self.konfiguracja.loc['Silhouette_klasyfikacja', 'random_state'] = self.ui.spinBoxRandomState.value()
                self.konfiguracja.loc['Silhouette_klasyfikacja', 'min_samples_leaf'] = self.ui.spinBoxMinSamplesLeaf.value()
                self.konfiguracja.loc['Silhouette_klasyfikacja', 'min_samples_split'] = self.ui.spinBoxMinSamplesSplit.value()
                self.konfiguracja.loc['Silhouette_klasyfikacja', 'splitter'] = self.ui.lineEditSpliter.text()
            elif self.ui.comboBoxWyborMiar.currentIndex() == 1:
                self.konfiguracja.loc['DaviesBouldin_klasyfikacja', 'criterion'] = self.ui.lineEditCriterion.text()
                if self.ui.checkBoxMaxDepthNone.isChecked():
                    self.konfiguracja.loc['DaviesBouldin_klasyfikacja', 'max_depth'] = 'None'
                else:
                    self.konfiguracja.loc['DaviesBouldin_klasyfikacja', 'max_depth'] = int(self.ui.spinBoxMaxDepth.value())
                self.konfiguracja.loc['DaviesBouldin_klasyfikacja', 'random_state'] = self.ui.spinBoxRandomState.value()
                self.konfiguracja.loc[
                    'DaviesBouldin_klasyfikacja', 'min_samples_leaf'] = self.ui.spinBoxMinSamplesLeaf.value()
                self.konfiguracja.loc[
                    'DaviesBouldin_klasyfikacja', 'min_samples_split'] = self.ui.spinBoxMinSamplesSplit.value()
                self.konfiguracja.loc['DaviesBouldin_klasyfikacja', 'splitter'] = self.ui.lineEditSpliter.text()
            elif self.ui.comboBoxWyborMiar.currentIndex() == 2:
                self.konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'criterion'] = self.ui.lineEditCriterion.text()
                if self.ui.checkBoxMaxDepthNone.isChecked():
                    self.konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'max_depth'] = 'None'
                else:
                    self.konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'max_depth'] = int(self.ui.spinBoxMaxDepth.value())
                self.konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'random_state'] = self.ui.spinBoxRandomState.value()
                self.konfiguracja.loc[
                    'CalinskiHarabasz_klasyfikacja', 'min_samples_leaf'] = self.ui.spinBoxMinSamplesLeaf.value()
                self.konfiguracja.loc[
                    'CalinskiHarabasz_klasyfikacja', 'min_samples_split'] = self.ui.spinBoxMinSamplesSplit.value()
                self.konfiguracja.loc['CalinskiHarabasz_klasyfikacja', 'splitter'] = self.ui.lineEditSpliter.text()
        elif self.ui.comboBoxWyborKlasyfikatora.currentIndex() == 1:
            if self.ui.comboBoxWyborMiar.currentIndex() == 0:
                self.konfiguracja.loc['Silhouette_regresja', 'criterion'] = self.ui.lineEditCriterion.text()
                if self.ui.checkBoxMaxDepthNone.isChecked():
                    self.konfiguracja.loc['Silhouette_regresja', 'max_depth'] = 'None'
                else:
                    self.konfiguracja.loc[
                        'Silhouette_regresja', 'max_depth'] = int(self.ui.spinBoxMaxDepth.value())
                self.konfiguracja.loc[
                    'Silhouette_regresja', 'random_state'] = self.ui.spinBoxRandomState.value()
                self.konfiguracja.loc[
                    'Silhouette_regresja', 'min_samples_leaf'] = self.ui.spinBoxMinSamplesLeaf.value()
                self.konfiguracja.loc[
                    'Silhouette_regresja', 'min_samples_split'] = self.ui.spinBoxMinSamplesSplit.value()
                self.konfiguracja.loc['Silhouette_regresja', 'splitter'] = self.ui.lineEditSpliter.text()
            elif self.ui.comboBoxWyborMiar.currentIndex() == 1:
                self.konfiguracja.loc['DaviesBouldin_regresja', 'criterion'] = self.ui.lineEditCriterion.text()
                if self.ui.checkBoxMaxDepthNone.isChecked():
                    self.konfiguracja.loc['DaviesBouldin_regresja', 'max_depth'] = 'None'
                else:
                    self.konfiguracja.loc[
                        'DaviesBouldin_regresja', 'max_depth'] = int(self.ui.spinBoxMaxDepth.value())
                self.konfiguracja.loc[
                    'DaviesBouldin_regresja', 'random_state'] = self.ui.spinBoxRandomState.value()
                self.konfiguracja.loc[
                    'DaviesBouldin_regresja', 'min_samples_leaf'] = self.ui.spinBoxMinSamplesLeaf.value()
                self.konfiguracja.loc[
                    'DaviesBouldin_regresja', 'min_samples_split'] = self.ui.spinBoxMinSamplesSplit.value()
                self.konfiguracja.loc['DaviesBouldin_regresja', 'splitter'] = self.ui.lineEditSpliter.text()
            elif self.ui.comboBoxWyborMiar.currentIndex() == 2:
                self.konfiguracja.loc['CalinskiHarabasz_regresja', 'criterion'] = self.ui.lineEditCriterion.text()
                if self.ui.checkBoxMaxDepthNone.isChecked():
                    self.konfiguracja.loc['CalinskiHarabasz_regresja', 'max_depth'] = 'None'
                else:
                    self.konfiguracja.loc[
                        'CalinskiHarabasz_regresja', 'max_depth'] = int(self.ui.spinBoxMaxDepth.value())
                self.konfiguracja.loc[
                    'CalinskiHarabasz_regresja', 'random_state'] = self.ui.spinBoxRandomState.value()
                self.konfiguracja.loc[
                    'CalinskiHarabasz_regresja', 'min_samples_leaf'] = self.ui.spinBoxMinSamplesLeaf.value()
                self.konfiguracja.loc[
                    'CalinskiHarabasz_regresja', 'min_samples_split'] = self.ui.spinBoxMinSamplesSplit.value()
                self.konfiguracja.loc['CalinskiHarabasz_regresja', 'splitter'] = self.ui.lineEditSpliter.text()

        self.konfiguracja.to_csv('Funkcje/Klasyfikator/properties.csv')

