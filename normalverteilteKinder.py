import numpy as np
from numpy.random import seed
from numpy.random import normal
import matplotlib.pyplot as plt
from scipy.stats import truncnorm

# Änderung der Parameter des truncnorm Befehls zur vereinfachten Bedienung --------------------------------------------/
def get_truncated_normal(Mittelwert=0, Standardabweichung=1, untereGrenze=-10, obereGrenze=10):
    return truncnorm(
        (untereGrenze - Mittelwert) / Standardabweichung, (obereGrenze - Mittelwert) / Standardabweichung,
        loc   = Mittelwert,
        scale = Standardabweichung
    )

# Entscheide ob ich das Kind behalten soll, oder nicht. Behalten = True, Entfernen = False ----------------------------/
def KindBehalten(x_vec_Kind, minD):
    behalten = False
    for i in range(len(x_vec_Kind)):
        if x_vec_Kind[i] > minD or x_vec_Kind[i] < - minD:
            behalten = True
        else:
            continue
    return behalten

# Deklarieren ---------------------------------------------------------------------------------------------------------/
def normalverteilteKinder(C2 = 0.1, n = 20, maxD = 4, x_vec_Eltern = np.array([2., 3., 1.])):
    # Initialisieren ------------------------------------------------------------------------------------------------------/
    minD    = C2 * maxD    # Box minimal
    x_vec_Kind_lokal = np.zeros(3)
    x_vec_Kind_global= np.zeros(3)
    Kinder = np.empty(3)    # Pro Zeile steht ein Kind (x1, x2, x3)

    # Sammel 20 valide Kinder ---------------------------------------------------------------------------------------------/
    while len(Kinder) < n:
        # Lokales Kind erstellen ------------------------------------------------------------------------------------------/
        for i in range(len(x_vec_Kind_lokal)):
            x_i_Kind_rdm = get_truncated_normal(Mittelwert          = 0,
                                                Standardabweichung  = maxD/3,
                                                untereGrenze        = -maxD,
                                                obereGrenze         = maxD
                                                )
            x_i_Kind_lokal = x_i_Kind_rdm.rvs()
            x_vec_Kind_lokal[i] = x_i_Kind_lokal

        # Überprüfen, ob Kind innerhalb der Suchbox -----------------------------------------------------------------------/
        if KindBehalten(x_vec_Kind_lokal, minD) == True:
            x_vec_Kind_global = x_vec_Kind_lokal + x_vec_Eltern
            Kinder = np.vstack([Kinder,x_vec_Kind_global])
    return Kinder

print(normalverteilteKinder())
