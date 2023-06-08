"""Beleg 3 - Modifizierte Evolutionsstrategie | 08/06/2023"""


import random
import copy as cp
import numpy as np                          # Paket für numerische Operationen
import matplotlib.pyplot as plt             # Paket fürs grafische Darstellen
from matplotlib import rc


# zufälligen Startpunkt erstellen
x = np.ndarray(shape=(3,))
x[0] = random.uniform(nb[0,0],nb[0,1]) #x1 Richtung
x[1] = random.uniform(nb[1,0],nb[1,1]) #x2 Richtung
x[2] = random.uniform(nb[2,0],nb[2,1]) #x3 Richtung


# Nebenbedingungen festlegen
nb = np.ndarray(shape=(3, 2))
nb[0, :] = [-np.pi, np.pi]        # Nebenbedingung in x1 Richtung
nb[1, :] = [-np.pi, np.pi]        # Nebenbedingung in x2 Richtung
nb[2, :] = [-np.pi, np.pi]

# Zielfunktionswert berechnen
def zf(xVec):
    """
    Definiton Zielfunktion

    :param xVec: Punkt im Eingangsraum
    :return: zugehörigen Zielfunktionswert
    """

    z = np.sin([xVec[0]]) + 7 * np.sin(xVec[1])**2 + 0.1 * xVec[2]**4 * np.sin(xVec[0])
    return z



# Suchbereich festlegen

# Normalverteilt Kinder erstellen
