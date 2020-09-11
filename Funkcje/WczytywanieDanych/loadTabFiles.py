import pandas as pd
import csv
from itertools import islice
import re
import numpy as np

def loadTabFiles(dane):
    liczbaWierszy = sum(1 for line in open(dane))
    nazwyAtrybutow = ''
    daneJakoListy = []
    iloscAtrybutow = 0
    with open(dane, newline='') as data:
        daneZPliku = csv.reader(data, delimiter='\t')
        wiersz = next(daneZPliku)
        wierszString = wiersz[0]
        iloscAtrybutow = int(re.search(r'\d+', wierszString).group())
        for i in islice(daneZPliku, 0, iloscAtrybutow):
            naglowekKolumny = str(i[0]).split(maxsplit=10)
            nazwyAtrybutow = nazwyAtrybutow + ' ' + naglowekKolumny[0]
        daneJakoListy.append(nazwyAtrybutow.split())
        for j in islice(daneZPliku, 1, liczbaWierszy):
            if len(j) == iloscAtrybutow:
                daneJakoListy.append(j)
                continue
            wierszPodzielony = [i.strip() for i in j]
            wierszPodzielony = [i.split() for i in j]
            daneJakoListy.append(wierszPodzielony)

    daneGotowe = np.vstack(tuple(daneJakoListy))
    df = pd.DataFrame(daneGotowe)
    headers = df.iloc[0]
    daneDF = pd.DataFrame(df.values[1:], columns=headers)

    return daneDF