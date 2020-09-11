import pandas as pd

def loadNormalFilesWithHeader(dane, separator):
    daneDF = pd.read_csv(dane, sep=separator, header=0)
    return (daneDF)


def loadNormalFilesWithoutHeader(dane, separator):
    daneDF = pd.read_csv(dane, sep=separator, header=None)
    return (daneDF)