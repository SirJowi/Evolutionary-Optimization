"""Beleg 3 - Modifizierte Evolutionsstrategie | 08/06/2023"""


import random
import copy as cp
import numpy as np                          # Paket für numerische Operationen
import matplotlib.pyplot as plt             # Paket fürs grafische Darstellen
from matplotlib import rc
from normalverteilteKinder import *
from mpl_toolkits.mplot3d import Axes3D

# Nebenbedingungen festlegen
nb = np.ndarray(shape=(3, 2))
nb[0, :] = [-np.pi, np.pi]        # Nebenbedingung in x1 Richtung
nb[1, :] = [-np.pi, np.pi]        # Nebenbedingung in x2 Richtung
nb[2, :] = [-np.pi, np.pi]        # Nebenbedingung in x3 Richtung


# zufälligen Startpunkt erstellen
x = np.empty(3)
x[0] = random.uniform(nb[0,0],nb[0,1]) #x1 Richtung
x[1] = random.uniform(nb[1,0],nb[1,1]) #x2 Richtung
x[2] = random.uniform(nb[2,0],nb[2,1]) #x3 Richtung


# Definition des maximalen Suchbereiches
maxD = 4

runAnz = 500 # Anzahl der Iterationen
c1 = 0.5
c2 = 0.1
n = 10


zfHistory = []
xHistory = np.zeros(shape=(runAnz, 3))


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
def Erfolg(Kinder, x, n, maxD, c1):
    xNeu = []
    k = 0
    for i in range(n):
        # xNeu wird mit den Werten aus ZF befüllt
        xNeu.append(zf(Kinder[i, :]))

        # Abspeichern von verbesserten Werten
        if xNeu[i] > zf(x):
            k += 1

    # Überprüfung der Erfolgsregel
        if n / 5 > k:
            for j in range(k):
                if (nb[0, 0] <= Kinder[np.argmax(xNeu), 0] <= nb[0, 1] and nb[1, 0] <= Kinder[np.argmax(xNeu), 1] <= nb[1, 1] and nb[2, 0] <= Kinder[np.argmax(xNeu), 2] <= nb[2, 1]):
                    x[0] = Kinder[np.argmax(xNeu), 0]
                    x[1] = Kinder[np.argmax(xNeu), 1]
                    x[2] = Kinder[np.argmax(xNeu), 2]
                    print("Im Bereich drin: ", x)
                    return maxD, x
                # print("Erfolgsregel eingehalten")
                else:
                    if Kinder[np.argmax(xNeu), 0] < nb[0, 0]:
                        Kinder[np.argmax(xNeu), 0] = nb[0, 0]
                    elif Kinder[np.argmax(xNeu), 0] > nb[0, 1]:
                        Kinder[np.argmax(xNeu), 0] = nb[0, 1]

                    if Kinder[np.argmax(xNeu), 1] < nb[1, 0]:
                        Kinder[np.argmax(xNeu), 1] = nb[1, 0]
                    elif Kinder[np.argmax(xNeu), 1] > nb[1, 1]:
                        Kinder[np.argmax(xNeu), 1] = nb[1, 1]

                    if Kinder[np.argmax(xNeu), 2] < nb[2, 0]:
                        Kinder[np.argmax(xNeu), 2] = nb[2, 0]
                    elif Kinder[np.argmax(xNeu), 2] > nb[2, 1]:
                        Kinder[np.argmax(xNeu), 2] = nb[2, 1]
                    print("Bereich angepasst: ", x)
                    x[0] = Kinder[np.argmax(xNeu), 0]
                    x[1] = Kinder[np.argmax(xNeu), 1]
                    x[2] = Kinder[np.argmax(xNeu), 2]
            return maxD, x
        else:
            # print("Erfolgsregel nicht eingehalten")
            maxD = maxD * c1
            return maxD, x




def plotResults(zfHistory, xHistory):
    """
    :param zfHistory: Liste der Zielfunktionswerte
    :param xHistory: Verlaufsdaten der Parameter
    :return: None
    """

    fig = plt.figure(figsize=(12, 6))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122, projection='3d')

    # Optimierungsfortschritt
    ax1.plot(zfHistory, 'rx-', markersize=5, linewidth=1)
    ax1.set_yscale('log')
    ax1.set_title('Optimierungsfortschritt')
    ax1.set_ylabel('Zielfunktionswert')
    ax1.set_xlabel('Optimierungsiteration')
    ax1.grid()

    # Eingangsraumabsuche (x1, x2, x3)
    ax2.plot(xHistory[:, 0], xHistory[:, 1], xHistory[:, 2], 'bo-', markersize=5, linewidth=1)
    ax2.plot([xHistory[0, 0]], [xHistory[0, 1]], [xHistory[0, 2]], 'ro', markersize=5)
    ax2.set_title('Eingangsraumabsuche')
    ax2.set_xlabel('x1')
    ax2.set_ylabel('x2')
    ax2.set_zlabel('x3')
    ax2.grid()

    plt.show()

<<<<<<< HEAD
for p in range(4):
=======
>>>>>>> refs/remotes/origin/main

for i in range(runAnz):
    zfHistory.append(zf(x))
    xHistory[i, :] = cp.deepcopy(x)

    Kinder = normalverteilteKinder(c2, n, maxD, x)
    #print(Kinder)
    maxD, x = Erfolg(Kinder, x, n, maxD, c1)
    print("Funktionswert", zf(x))
    #print(i)

plotResults(zfHistory, xHistory)




