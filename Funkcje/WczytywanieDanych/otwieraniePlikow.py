import pandas as pd

from Funkcje.WczytywanieDanych.loadNormalFiles import loadNormalFilesWithoutHeader, loadNormalFilesWithHeader
from Funkcje.WczytywanieDanych.removeSymbolicValue import removeSymbolicValue


def otwieraniePlikow(dane):
    if '3D_spatial_network1.csv' in dane:
        daneDF = loadNormalFilesWithoutHeader(dane, ',')
    elif 'cluster_data.csv' in dane:
         daneDF = loadNormalFilesWithoutHeader(dane, ',')
    elif 'data_feature.csv' in dane:
        daneDF = loadNormalFilesWithoutHeader(dane, ',')
    elif 'supervision_cluster.csv' in dane:
        daneDF = loadNormalFilesWithoutHeader(dane, ',')
    elif 'xaaS.dat' in dane:
        daneDF = loadNormalFilesWithoutHeader(dane, ' ')
    elif 'xadS.dat' in dane:
        daneDF = loadNormalFilesWithoutHeader(dane, ' ')
    elif 'Absenteeism_at_work.csv' in dane:
        daneDF = loadNormalFilesWithHeader(dane, ';')
    elif '2018-04-2019-06-web-control.csv' in dane:
        daneDF = loadNormalFilesWithHeader(dane, ';')
    elif 'Data_Cortex_Nuclear.xls' in dane:
        daneDF = pd.read_excel(dane)
    elif 'QCM3.csv' in dane:
        daneDF = loadNormalFilesWithHeader(dane, ';')
    else:
        daneDF = loadNormalFilesWithHeader(dane, ',')

    if 'Frogs_MFCC.csv' in dane:
        danePrzygotowane = removeSymbolicValue(daneDF, dane)
    elif 'iBeacon_RSSI_LabeledS.csv' in dane:
        danePrzygotowane = removeSymbolicValue(daneDF, dane)
    elif 'online_shoppers_intention.csv' in dane:
        danePrzygotowane = removeSymbolicValue(daneDF, dane)
    elif 'Sales_Transactions_Dataset_Weekly.csv' in dane:
        danePrzygotowane = removeSymbolicValue(daneDF, dane)
    elif 'SCADI.csv' in dane:
        danePrzygotowane = removeSymbolicValue(daneDF, dane)
    elif 'xaaS.dat' in dane:
        danePrzygotowane = removeSymbolicValue(daneDF, dane)
    elif 'xadS.dat' in dane:
        danePrzygotowane = removeSymbolicValue(daneDF, dane)
    elif '2018-04-2019-06-web-control.csv' in dane:
        danePrzygotowane = removeSymbolicValue(daneDF, dane)
    elif 'a3_va3SD.csv' in dane:
        danePrzygotowane = removeSymbolicValue(daneDF, dane)
    elif 'buddymove_holidayiq.csv' in dane:
        danePrzygotowane = removeSymbolicValue(daneDF, dane)
    elif 'CC GENERAL.csv' in dane:
        danePrzygotowane = removeSymbolicValue(daneDF, dane)
    elif 'Data_Cortex_Nuclear.xls' in dane:
        danePrzygotowane = removeSymbolicValue(daneDF, dane)
    elif 'iris.data' in dane:
        danePrzygotowane = removeSymbolicValue(daneDF, dane)
    else:
        danePrzygotowane = daneDF

    return danePrzygotowane