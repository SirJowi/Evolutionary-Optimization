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
nb[2, :] = [-np.pi, np.pi]        # Nebenbedingung in x3 Richtung

# Definition des maximalen Suchbereiches
maxD = np.ndarray(shape=(3,))
maxD[0] = 10    # Suchbereich in x1 Richtung
maxD[1] = 10    # Suchbereich in x2 Richtung
maxD[2] = 10    # Suchbereich in x3 Richtung


# Definition der Optimierungsparameter



# Zielfunktionswert berechnen
def zf(xVec):
    """
    Definiton Zielfunktion

    :param xVec: Punkt im Eingangsraum
    :return: zugehörigen Zielfunktionswert
    """

    z = np.sin([xVec[0]]) + 7 * np.sin(xVec[1])**2 + 0.1 * xVec[2]**4 * np.sin(xVec[0])
    return z





#1/5 Erfolg
def Erfolg(A, x, n, maxD, c1):
    xNeu = []
    k = 0
    for i in range(n):
        #xNeu wird mit den Werten aus ZF befüllt
        xNeu.append(zf(A[i,:]))

        #Abspeichern von verbesserten Werten
        if xNeu[i] > zf(x):
            k += 1
            print(k)
    #Überprüfung der Erfolgsregel
    if n/5 > k:
        for j in range(k):#len(A)):
            if (nb[0, 0] <= A[np.argmax(xNeu), 0] <= nb[0, 1] and nb[1, 0] <= A[np.argmax(xNeu), 1] <= nb[1, 1] and nb[2, 0] <= A[np.argmax(xNeu), 2] <= nb[2, 1]):
                x[0] = A[np.argmax(xNeu),0]
                x[1] = A[np.argmax(xNeu),1]
                x[2] = A[np.argmax(xNeu),2]
            #print("Erfolgsregel eingehalten")
            else:
                if A[np.argmax(xNeu), 0] < nb[0, 0]:
                    A[np.argmax(xNeu), 0] = nb[0, 0]
                elif A[np.argmax(xNeu), 0] > nb[0, 1]:
                    A[np.argmax(xNeu), 0] = nb[0, 1]

                if A[np.argmax(xNeu), 1] < nb[1, 0]:
                    A[np.argmax(xNeu), 1] = nb[1, 0]
                elif A[np.argmax(xNeu), 1] > nb[1, 1]:
                    A[np.argmax(xNeu), 1] = nb[1, 1]

                if A[np.argmax(xNeu), 2] < nb[2, 0]:
                    A[np.argmax(xNeu), 2] = nb[2, 0]
                elif A[np.argmax(xNeu), 2] > nb[2, 1]:
                    A[np.argmax(xNeu), 2] = nb[2, 1]

                x[0] = A[np.argmax(xNeu),0]
                x[1] = A[np.argmax(xNeu),1]
                x[2] = A[np.argmax(xNeu),2]

    else:
        #print("Erfolgsregel nicht eingehalten")
        maxD = maxD * c1

#Erfolg(A, x, n, maxD, c1)



