import pandas as pd
from numpy import float64


def removeSymbolicValue(dane, nazwa):
    if nazwa in 'daneTreningowe/biodegSD.tab':
        dane['experimental_class'] = pd.factorize(dane['experimental_class'])[0] + 1
    if nazwa in 'daneTreningowe/ozoneS.tab':
        dane['Date'] = pd.factorize(dane['Date'])[0] + 1
    if nazwa in 'daneTreningowe/NoweDane/Frogs_MFCC.csv':
        dane['Species'] = pd.factorize(dane['Species'])[0] + 1
        dane['Genus'] = pd.factorize(dane['Genus'])[0] + 1
        dane['Family'] = pd.factorize(dane['Family'])[0] + 1
    if nazwa in 'daneTreningowe/NoweDane/iBeacon_RSSI_LabeledS.csv':
        dane['location'] = pd.factorize(dane['location'])[0] + 1
        dane['date'] = pd.factorize(dane['date'])[0] + 1
    if nazwa in 'daneTreningowe/NoweDane/online_shoppers_intention.csv':
        dane['Month'] = pd.factorize(dane['Month'])[0] + 1
        dane['VisitorType'] = pd.factorize(dane['VisitorType'])[0] + 1
        dane['Weekend'] = pd.factorize(dane['Weekend'])[0] + 1
        dane['Revenue'] = pd.factorize(dane['Revenue'])[0] + 1
    if nazwa in 'daneTreningowe/NoweDane/SCADI.csv':
        dane['Classes'] = pd.factorize(dane['Classes'])[0] + 1
    if nazwa in 'daneTreningowe/NoweDane/Sales_Transactions_Dataset_Weekly.csv':
        dane['Product_Code'] = pd.factorize(dane['Product_Code'])[0] + 1
    if nazwa in 'daneTreningowe/NoweDane/xaaS.dat':
        dane = dane[dane.columns[0:dane.shape[1]-1]]
        dane[dane.shape[1]-1] = pd.factorize(dane[dane.shape[1]-1])[0] + 1
    if nazwa in 'daneTreningowe/NoweDane/xadS.dat':
        dane = dane[dane.columns[0:dane.shape[1]-1]]
        dane[dane.shape[1]-1] = pd.factorize(dane[dane.shape[1]-1])[0] + 1
    if nazwa in'daneTreningowe/NoweDane/a3_va3SD.csv':
        dane['Class'] = pd.factorize(dane['Class'])[0] + 1
    if nazwa in 'daneTreningowe/NoweDane/buddymove_holidayiq.csv':
        dane['Id'] = pd.factorize(dane['Id'])[0] + 1
    if nazwa in 'daneTreningowe/NoweDane/Data_Cortex_Nuclear.xls':
        dane['Id'] = pd.factorize(dane['Id'])[0] + 1
        dane['Genotype'] = pd.factorize(dane['Genotype'])[0] + 1
        dane['Treatment'] = pd.factorize(dane['Treatment'])[0] + 1
        dane['Behavior'] = pd.factorize(dane['Behavior'])[0] + 1
        dane['Class'] = pd.factorize(dane['Class'])[0] + 1
    if nazwa in 'daneTreningowe/NoweDane/iris.data':
        dane['Class'] = pd.factorize(dane['Class'])[0] + 1
    if 'CC GENERAL.csv' in nazwa:
        dane['Id'] = pd.factorize(dane['Id'])[0] + 1
    if nazwa in 'daneTreningowe/NoweDane/1.csv':
        dane['Id'] = pd.factorize(dane['Id'])[0] + 1
    if nazwa in 'daneTreningowe/NoweDane/2018-04-2019-06-web-control.csv':
        dane['DATE'] = pd.factorize(dane['DATE'])[0] + 1
        dane['COUNTRY'] = pd.factorize(dane['COUNTRY'])[0] + 1
    return dane