import pandas as pd
import numpy as np
import functools
from tqdm import tqdm
from numpy import float64
from scipy.stats import shapiro, stats, normaltest
from scipy.stats import anderson


def liczCechy(dane, sciezka, czyAtrybutDecyzyjny, indeksAtrybutuDecyzyjnego, czyAtrybutIndeksujacy, indeksAtrybutuIndeksujacego):
    cechy = []
    daneDF = dane.copy()



    iloscWIerszy = daneDF.shape[0]
    iloscKolumn = daneDF.shape[1]

    ###############################ZMIANA WARTOSCI SYMBOLICZNYCH NA NUMERYCZNE#############

    if 'biodegSDC.tab' in sciezka:
        daneDF['experimental_class'] = pd.factorize(daneDF['experimental_class'])[0] + 1
    elif 'ozoneSDC.tab' in sciezka:
        daneDF['Date'] = pd.factorize(dane['Date'])[0] + 1
    elif '.tab' in sciezka:
        pass
    else:
        for i in range(0, iloscKolumn, 1):
            if 'object' in str(daneDF[daneDF.columns[i]].dtype):
                daneDF[daneDF.columns[i]] = pd.factorize(daneDF[daneDF.columns[i]])[0] + 1
            pass


    #################################UZUPELNIANIE i PUSTE##################################

    pusteKolumna = []
    pusteCaleDane = 0
    sredniaIloscPustych = 0
    pusteAtrybut = 0

    for j in tqdm(range(0, iloscKolumn), desc= 'Kolumny', dynamic_ncols=True):
        for i in range(0, iloscWIerszy):
            komorka = pd.to_numeric(daneDF.iloc[i, j], errors='coerce')
            if pd.isna(komorka):
                pusteCaleDane += 1
                pusteAtrybut += 1
                if czyAtrybutDecyzyjny:
                    atrybutDecyzyjnyNazwa = list(daneDF.columns.values)[indeksAtrybutuDecyzyjnego-1]
                    klasaDlaTegoWiersza = daneDF.iloc[i, indeksAtrybutuDecyzyjnego - 1]
                    daneKopia2 = daneDF.loc[daneDF[atrybutDecyzyjnyNazwa] == klasaDlaTegoWiersza]
                    daneKopia3 = daneKopia2[daneKopia2.columns.values[j]]
                    daneKopia3 = pd.to_numeric(daneKopia3, errors= 'coerce')
                    srednia = np.mean(daneKopia3).round(2)
                    moda = daneKopia3.mode()
                    moda = moda[0]
                    if daneKopia3.nunique() <= 20:
                        daneDF.iat[i, j] = moda
                    if daneKopia3.nunique() > 20:
                        daneDF.iat[i, j] = srednia
                else:
                    daneKopia2 = daneDF[daneDF.columns.values[j]]
                    srednia = np.mean(daneKopia2).round(2)
                    moda = daneKopia2.mode()
                    moda = moda[0]
                    if daneKopia2.nunique() <= 20:
                        daneDF.iat[i, j] = moda
                    if daneKopia2.nunique() > 20:
                        daneDF.iat[i, j] = srednia

        pusteKolumna.append(pusteAtrybut)
        pusteAtrybut = 0

    sredniaIloscPustych = functools.reduce(lambda x, y: x + y, pusteKolumna)
    sredniaIloscPustych = sredniaIloscPustych / (iloscKolumn)

    minIloscPustych = min(pusteKolumna)
    maxIloscPustych = max(pusteKolumna)

    #print("Ile pustych wartosci")
    #print(pusteKolumna)
    #print(pusteCaleDane)
    #print(sredniaIloscPustych)
        ############################################################################

        ###################################################################
    daneWyznaczanieWartosci = daneDF.copy()
    if czyAtrybutIndeksujacy:
        daneWyznaczanieWartosci = daneWyznaczanieWartosci.drop(daneWyznaczanieWartosci.columns[indeksAtrybutuIndeksujacego], axis=1)

    sredniaZKolumn = []
    sredniaWszystkichDanych = 0

    medianaZKolumn = []
    medianaWszystkichDanych = 0

    modaZKolumn = []
    sredniaModaWszystkichKolumn = 0

    odchylenieStandardoweWKolumnie = []
    srednieodchylenieStandardowe = 0

    wariancjaWKolumnie = []
    sredniaWariancja = 0

    odchylenieStandardoweWKolumnie = []
    srednieodchylenieStandardowe = 0

    wariancjaWKolumnie = []
    sredniaWariancja = 0

    skosnoscWKolumnie = []
    sredniaSkosnosc = 0

    kurtozaWKolumnie = []
    sredniaKurtoza = 0

    minWKolumnie = []
    srednieMin = 0

    maxWKolumnie = []
    srednieMax = 0

    kwartyl25ProcWKolumnie = []
    sredniKwartyl25Proc = 0

    kwartyl50ProcWKolumnie = []
    sredniKwartyl50Proc = 0

    kwartyl75ProcWKolumnie = []
    sredniKwartyl75Proc = 0

    rozstepWKolumnie = []
    sredniRozstep = 0

    ileAtrybutow = daneWyznaczanieWartosci.shape[1]
    for i in range(0, ileAtrybutow, 1):

        bufor = daneWyznaczanieWartosci[daneWyznaczanieWartosci.columns[i]]
        bufor = pd.to_numeric(bufor)

        srednia = bufor.describe()[1]
        sredniaZKolumn.append(srednia)

        mediana = np.median(bufor)
        medianaZKolumn.append(mediana)

        moda = bufor.mode()
        moda = moda[0]
        modaZKolumn.append(moda)

        odchylenieStandardowe = bufor.describe()[2]
        odchylenieStandardoweWKolumnie.append(odchylenieStandardowe)

        wariancja = bufor.var()
        wariancjaWKolumnie.append(wariancja)

        skosnosc = bufor.skew()
        skosnoscWKolumnie.append(skosnosc)

        kurtoza = bufor.kurt()
        kurtozaWKolumnie.append(kurtoza)

        minWartosc = bufor.min()
        minWKolumnie.append(minWartosc)

        maxWartosc = bufor.max()
        maxWKolumnie.append(maxWartosc)

        kwartyl25Proc = bufor.describe()[4]
        kwartyl25ProcWKolumnie.append(kwartyl25Proc)

        kwartyl50Proc = bufor.describe()[5]
        kwartyl50ProcWKolumnie.append(kwartyl50Proc)

        kwartyl75Proc = bufor.describe()[6]
        kwartyl75ProcWKolumnie.append(kwartyl75Proc)

        rozstep = maxWartosc - minWartosc
        rozstepWKolumnie.append(rozstep)


    sredniaWszystkichDanych = functools.reduce(lambda x, y: x + y, sredniaZKolumn)
    sredniaWszystkichDanych = sredniaWszystkichDanych / (ileAtrybutow)

    minSrednia = min(sredniaZKolumn)
    maxSrednia = max(sredniaZKolumn)

    sredniaMedianaWszystkichDanych = functools.reduce(lambda x, y: x + y, medianaZKolumn)
    sredniaMedianaWszystkichDanych = sredniaMedianaWszystkichDanych / (ileAtrybutow)

    minMediana = min(medianaZKolumn)
    maxMediana = max(medianaZKolumn)

    sredniaModaWszystkichKolumn = functools.reduce(lambda x, y: x + y, modaZKolumn)
    sredniaModaWszystkichKolumn = sredniaModaWszystkichKolumn / (ileAtrybutow)

    minModa = min(modaZKolumn)
    maxModa = max(modaZKolumn)

    srednieodchylenieStandardowe = functools.reduce(lambda x, y: x + y, odchylenieStandardoweWKolumnie)
    srednieodchylenieStandardowe = srednieodchylenieStandardowe / (ileAtrybutow)

    minOdchylenieStandardowe = min(odchylenieStandardoweWKolumnie)
    maxOdchylenieStandardowe = max(odchylenieStandardoweWKolumnie)

    sredniaWariancja = functools.reduce(lambda x, y: x + y, wariancjaWKolumnie)
    sredniaWariancja = sredniaWariancja / (ileAtrybutow)

    minWariancja = min(wariancjaWKolumnie)
    maxWariancja = max(wariancjaWKolumnie)

    sredniaSkosnosc = functools.reduce(lambda x, y: x + y, skosnoscWKolumnie)
    sredniaSkosnosc = sredniaSkosnosc / (ileAtrybutow)

    minSkosnosc = min(skosnoscWKolumnie)
    maxSkosnosc = max(skosnoscWKolumnie)

    sredniaKurtoza = functools.reduce(lambda x, y: x + y, kurtozaWKolumnie)
    sredniaKurtoza = sredniaKurtoza / (ileAtrybutow )

    minKurtoza = min(kurtozaWKolumnie)
    maxKurtoza = max(kurtozaWKolumnie)

    srednieMin = functools.reduce(lambda x, y: x + y, minWKolumnie)
    srednieMin = srednieMin / (ileAtrybutow)

    minMinWartosc = min(minWKolumnie)
    maxMinWartosc = max(minWKolumnie)

    srednieMax = functools.reduce(lambda x, y: x + y, maxWKolumnie)
    srednieMax = srednieMax / (ileAtrybutow)

    minMaxWartosc = min(maxWKolumnie)
    maxMaxWartosc = max(maxWKolumnie)

    sredniKwartyl25Proc = functools.reduce(lambda x, y: x + y, kwartyl25ProcWKolumnie)
    sredniKwartyl25Proc = sredniKwartyl25Proc / (ileAtrybutow)

    minKwartyl25 = min(kwartyl25ProcWKolumnie)
    maxKwartyl25 = max(kwartyl25ProcWKolumnie)

    sredniKwartyl50Proc = functools.reduce(lambda x, y: x + y, kwartyl50ProcWKolumnie)
    sredniKwartyl50Proc = sredniKwartyl50Proc / (ileAtrybutow)

    minKwartyl50 = min(kwartyl50ProcWKolumnie)
    maxKwartyl50 = max(kwartyl50ProcWKolumnie)

    sredniKwartyl75Proc = functools.reduce(lambda x, y: x + y, kwartyl75ProcWKolumnie)
    sredniKwartyl75Proc = sredniKwartyl75Proc / (ileAtrybutow)

    minKwartyl75 = min(kwartyl75ProcWKolumnie)
    maxKwartyl75 = max(kwartyl75ProcWKolumnie)

    sredniRozstep = functools.reduce(lambda x, y: x + y, rozstepWKolumnie)
    sredniRozstep = sredniRozstep / (ileAtrybutow)

    minRozstep = min(rozstepWKolumnie)
    maxRozstep = max(rozstepWKolumnie)

    #########################################################################

    #################ILE UNIKALNYCH WARTOSCI W KLASIE #################

    if czyAtrybutDecyzyjny:
        ileUnikalnychWartosciAD = daneDF[daneDF.columns[indeksAtrybutuDecyzyjnego - 1]].nunique()
    else:
        ileUnikalnychWartosciAD = 0

    ##print("Liczba unikalnych wartosci w klasie")
    ##print(ileUnikalnychWartosciAD)

    ########################################################################

    #####################LICZBA UNIKALNYCH WARTOŚCI W KOLUMNIE##############

    ileUnikalnychWartosciWKolumnie = []
    sredniaIloscUnikalnychWartosci = 0

    for i in range(0, ileAtrybutow, 1):

        ileUnikalnychWartosci = daneWyznaczanieWartosci[daneWyznaczanieWartosci.columns[i]].nunique()
        ileUnikalnychWartosciWKolumnie.append(ileUnikalnychWartosci)

    sredniaIloscUnikalnychWartosci = functools.reduce(lambda x, y: x + y, ileUnikalnychWartosciWKolumnie)
    sredniaIloscUnikalnychWartosci = sredniaIloscUnikalnychWartosci / (ileAtrybutow)

    minIloscUnikalnychWartosci = min(ileUnikalnychWartosciWKolumnie)
    maxIloscUnikalnychWartosci = max(ileUnikalnychWartosciWKolumnie)

    #print("Liczba unikalnych wartosci")
    ##print(ileUnikalnychWartosciWKolumnie)
    ##print(sredniaIloscUnikalnychWartosci)

    #########################################################################

    ########################ROZKLAD NORMALNY###############################
    daneTestNormalnosci = daneDF.copy()
    rozkladNormalnyShapiroTakNie = 0
    rozkladNormalnyAndersonDarlingTakNie = 0
    rozkladNormalnyDAgostinosTakNie = 0
    rozkladNormalnyAndersonDarling = 0

    ####SHAPIRO
    testRozkladuShapiro = daneTestNormalnosci.to_numpy(dtype=float64)
    stat, p = shapiro(testRozkladuShapiro)
    alpha = 0.05
    if p > alpha:
        rozkladNormalnyShapiroTakNie = 1
    else:
        rozkladNormalnyShapiroTakNie = 0


    ####D’Agostino’s
    testRozkladuDAgostinos = daneTestNormalnosci.to_numpy(dtype=float64)
    # for j in range(0, iloscKolumn):
    #     if daneKopia.columns[0] == 0 and daneKopia.columns[1] == 1:
    #         stat, p = stats.normaltest(testRozkladuDAgostinos[j])
    #     else:
    #         stat, p = stats.normaltest(testRozkladuDAgostinos[testRozkladuDAgostinos.columns[j]])
    #
    #     ##print('Statistics=%.3f, p=%.3f' % (stat, p))
    #     alpha = 0.05
    #     if p > alpha:
    #         rozkladNormalnyDAgostinos += 1
    #
    #     ##print("Rozkład normalny D’Agostino’s")
    #     ##print(str(rozkladNormalnyDAgostinos) + " " + str(iloscKolumn))
    # if rozkladNormalnyDAgostinos < iloscKolumn:
    #     rozkladNormalnyDAgostinosTakNie = 0
    # else:
    #     rozkladNormalnyDAgostinosTakNie = 1
    stat1, p2 = stats.normaltest(testRozkladuDAgostinos)
    alpha = 0.05
    if p2.all() > alpha:
        rozkladNormalnyDAgostinosTakNie = 1
    else:
        rozkladNormalnyDAgostinosTakNie = 0

    ####Anderson-Darling
    testRozkladuAndersonDarling = daneTestNormalnosci.copy()
    testRozkladuAndersonDarling = testRozkladuAndersonDarling.astype(float64)
    for j in range(0, iloscKolumn):
        if testRozkladuAndersonDarling.columns[0] == 0 and testRozkladuAndersonDarling.columns[1] == 1:
            result = anderson(testRozkladuAndersonDarling[j])
        else:
            result = anderson(testRozkladuAndersonDarling[testRozkladuAndersonDarling.columns[j]])

        for i in range(len(result.critical_values)):
            sl, cv = result.significance_level[i], result.critical_values[i]
            if result.statistic < result.critical_values[i]:
                #print('%.3f: %.3f, data looks normal (fail to reject H0)' % (sl, cv))
                #print(result.statistic)
                pass
            else:
                ##print('%.3f: %.3f, data does not look normal (reject H0)' % (sl, cv))
                ##print(result.statistic)
                break
            rozkladNormalnyAndersonDarling += 1
    ##print(str(rozkladNormalnyAndersonDarling) + " " + str(iloscKolumn))
    if rozkladNormalnyAndersonDarling < iloscKolumn:
        rozkladNormalnyAndersonDarlingTakNie = 0
    else:
        rozkladNormalnyAndersonDarlingTakNie = 1
    ##print("Rozkład normalny Anderson-Darling")
    #print(rozkladNormalnyAndersonDarlingTakNie)



    cechy = {"Ile wierszy" : iloscWIerszy,
                "Ile atrybutów" : iloscKolumn,
                "Ilość pustych wartości" :pusteCaleDane,
                "Minimalna ilość pustych w kolumach" : minIloscPustych,
                "Średnia ilosc pustych w kolumnach" : sredniaIloscPustych,
                "Maksymalna ilosc pustych w kolumnach" : maxIloscPustych,
                "Minimalna srednia w kolumnach" : minSrednia,
                "Srednia średnich" : sredniaWszystkichDanych,
                "Maksymalna srednia w kolumnach" : maxSrednia,
                "Minimalna mediana" : minMediana,
                "Średnia mediana danych" : sredniaMedianaWszystkichDanych,
                "Maksymalna mediana" : maxMediana,
                "Minimalna moda" : minModa,
                "Średnia moda danych" : sredniaModaWszystkichKolumn,
                "Maksymalna moda" : maxModa,
                "Minimalne odchylenie standardowe" : minOdchylenieStandardowe,
                "Średnie odchylenie standardowe" : srednieodchylenieStandardowe,
                "Maksymalne odchylenie standardowe" : maxOdchylenieStandardowe,
                "Minimalna wariancja" : minWariancja,
                "Średnia wariancja" : sredniaWariancja,
                "Maksymalna wariancja" : maxWariancja,
                "Minimalna skośność" : minSkosnosc,
                "Średnia skośność" : sredniaSkosnosc,
                "Maksymalna skośność" : maxSkosnosc,
                "Minimalna kurtoza" : minKurtoza,
                "Średnia kurtoza" : sredniaKurtoza,
                "Maksymalna kurtoza" : maxKurtoza,
                "Minimalna wartosc danych" : minMinWartosc,
                "Maksymalna wartość w danych" : maxMaxWartosc,
                "Minimalny kwartyl 25%" : minKwartyl25,
                "Średni kwartyl 25%" : sredniKwartyl25Proc,
                "Maksymalny kwartyl 25%" : maxKwartyl25,
                "Minimalny kwartyl 50%" : minKwartyl50,
                "Średni kwartyl 50%" : sredniKwartyl50Proc,
                "Maksymalny kwartyl 50%" : maxKwartyl50,
                "Minimalny kwartyl 75%" : minKwartyl75,
                "Średni kwartyl 75%": sredniKwartyl75Proc,
                "Maksymalny kwartyl 75%" : maxKwartyl75,
                "Minimalny rozstęp" : minRozstep,
                "Średni rozstęp" : sredniRozstep,
                "Maksymalny rozstęp" : maxRozstep,
                "Ilość unikalnych wartości atrybutu decyzyjnego" : ileUnikalnychWartosciAD,
                "Minimalna liczba unikalnych wartości" : minIloscUnikalnychWartosci,
                "Średnia ilość unikalnych wartości atrybutów" : sredniaIloscUnikalnychWartosci,
                "Maksymalna liczba unikalnych wartości" : maxIloscUnikalnychWartosci,
                "Rozkład normalny Shapiro" : rozkladNormalnyShapiroTakNie,
                "Rozkład normalny D’Agostino’s" : rozkladNormalnyDAgostinosTakNie,
                "Rozkład normalny Anderson-Darling" : rozkladNormalnyAndersonDarlingTakNie}


    return cechy, daneDF

