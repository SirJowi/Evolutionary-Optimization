"""Beleg 3 - Modifizierte Evolutionsstrategie | 08/06/2023"""

import random
import copy as cp
import numpy as np                          # Paket für numerische Operationen
import matplotlib.pyplot as plt             # Paket fürs grafische Darstellen
from matplotlib import rc
from normalverteilteKinder import *
from mpl_toolkits.mplot3d import Axes3D

#-----------------------------------------------------------------------------------------------------

maxD = 1.0 # Definition des maximalen Suchbereiches
runAnz = 50 # Anzahl der Iterationen
anzKett = 9 #Anzahl der Ketten
c1 = 0.5 # Faktor mit dem maxD verkleinert wird bei 1/5 Regel
c2 = 0.1 # minD / maxD
n = 25 #Anzahl der Kinder
mm = 1 #Min = -1 oder Max = +1

#-----------------------------------------------------------------------------------------------------

# Nebenbedingungen festlegen
nb = np.ndarray(shape=(3, 2))
nb[0, :] = [-np.pi, np.pi]        # Nebenbedingung in x1 Richtung
nb[1, :] = [-np.pi, np.pi]        # Nebenbedingung in x2 Richtung
nb[2, :] = [-np.pi, np.pi]        # Nebenbedingung in x3 Richtung


# zufälligen Startpunkt erstellen
def Startpunkt():
    x = np.empty(3)
    x[0] = random.uniform(nb[0,0],nb[0,1]) #x1 Richtung
    x[1] = random.uniform(nb[1,0],nb[1,1]) #x2 Richtung
    x[2] = random.uniform(nb[2,0],nb[2,1]) #x3 Richtung
    return x

#-----------------------------------------------------------------------------------------------------

#Variablen für Plots
zfHistory = []
xHistory = np.zeros(shape=(runAnz, 3))

#-----------------------------------------------------------------------------------------------------


# Zielfunktionswert berechnen
def zf(xVec):
    """
    Definiton Zielfunktion

    :param xVec: Punkt im Eingangsraum
    :return: zugehörigen Zielfunktionswert
    """

    z = mm*(np.sin([xVec[0]]) + 7 * np.sin(xVec[1])**2 + 0.1 * xVec[2]**4 * np.sin(xVec[0]))
    return z

#-----------------------------------------------------------------------------------------------------

#1/5 Erfolg und Nebenbedingung
def Erfolg(Kinder, x, n, maxD, c1):
    xNeu = []
    k = 0
    for i in range(n):
        # xNeu wird mit den Werten aus ZF befüllt
        xNeu.append(zf(Kinder[i, :]))

        # Hochzählen wieviele Werte besser sind
        if xNeu[i] > zf(x):
            k += 1
            #print("k:",k)
    # Überprüfung der Erfolgsregel
        if n / 5 > k:
            for j in range(k):
                # Wenn Erfolgsregel erfüllt ist, werden die Koordinaten des besten Kindes zum neuen Elternpunkt
                if (nb[0, 0] <= Kinder[np.argmax(xNeu), 0] <= nb[0, 1] and nb[1, 0] <= Kinder[np.argmax(xNeu), 1] <= nb[1, 1] and nb[2, 0] <= Kinder[np.argmax(xNeu), 2] <= nb[2, 1]):
                    x[0] = Kinder[np.argmax(xNeu), 0]
                    x[1] = Kinder[np.argmax(xNeu), 1]
                    x[2] = Kinder[np.argmax(xNeu), 2]
                    return maxD, x
                else:
                    #print("RB verletzt")
                    # Wenn die Erfolgsregel nicht eingehalten wird:
                    # Fakultativ: jeweilige Über-/Unterschreitung der NB, wird der jeweilige Wert zurück auf den Rand gesetzt
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

                    # Koordinaten des besten Kindes zum neuen Elternpunkt
                    x[0] = Kinder[np.argmax(xNeu), 0]
                    x[1] = Kinder[np.argmax(xNeu), 1]
                    x[2] = Kinder[np.argmax(xNeu), 2]
            return maxD, x
        else:
            # Wenn Erfolgsregel nicht erfüllt, wird der Suchbereich verkleinert
            maxD = maxD * c1
            return maxD, x

#-----------------------------------------------------------------------------------------------------

def plotResults(zfHistory, xHistory, anzKett):
    """
    :param zfHistory: Liste der Zielfunktionswerte
    :param xHistory: Verlaufsdaten der Parameter
    :param anzKett: Anzahl der Ketten
    :return: None
    """

    fig = plt.figure(figsize=(12, 6))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122, projection='3d')

    colors = plt.cm.rainbow(np.linspace(0, 1, anzKett))  # Farben für die Ketten

    # Optimierungsfortschritt
    for p in range(anzKett):
        ax1.plot(zfHistory[p::anzKett], 'x-', markersize=5, linewidth=1, color=colors[p], label=f'Schleife {p+1}')
    ax1.set_yscale('log')
    ax1.set_title('Optimierungsfortschritt')
    ax1.set_ylabel('Zielfunktionswert')
    ax1.set_xlabel('Optimierungsiteration')
    ax1.grid()
    ax1.legend()

    # Eingangsraumabsuche (x1, x2, x3)
    for p in range(anzKett):
        ax2.plot(xHistory[:, 0][p::anzKett], xHistory[:, 1][p::anzKett], xHistory[:, 2][p::anzKett], 'o-', markersize=5, linewidth=1, color=colors[p], label=f'Schleife {p+1}')
    ax2.plot([xHistory[0, 0]], [xHistory[0, 1]], [xHistory[0, 2]], 'ro', markersize=5)
    ax2.set_title('Eingangsraumabsuche')
    ax2.set_xlabel('x1')
    ax2.set_ylabel('x2')
    ax2.set_zlabel('x3')
    ax2.grid()
    ax2.legend()

    plt.show()

#-----------------------------------------------------------------------------------------------------
maxF = 0
print("\t Kette\t| Startpunkt/Zielpunkt\t\t\t\t\t\t| Zielpunkt")
print("\t-------------------------------------------------------------------")
for p in range(anzKett):
    x = Startpunkt()
    print("\t\t\t|", x, "\t|")
    for i in range(runAnz):

        zfHistory.append(zf(x))
        xHistory[i, :] = cp.deepcopy(x)

        Kinder = normalverteilteKinder(c2, n, maxD, x)

        maxD, x = Erfolg(Kinder, x, n, maxD, c1)

    print("\t", p + 1, "\t\t|", x,"\t|", zf(x))
    print("\t-------------------------------------------------------------------")

    if zf(x) > maxF:
        maxKette = p
        maxF = zf(x)
        maxx = x
#-----------------------------------------------------------------------------------------------------

print("")
print("\t-----Suche abgeschlossen-------------------------------------------")
print("\t", maxKette, "\t\t|", x,"\t|", maxF)

plotResults(zfHistory, xHistory,anzKett)





