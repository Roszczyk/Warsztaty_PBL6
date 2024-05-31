# Importowanie wymaganych bibliotek
import numpy as np
class ANN:
    def __init__(self, inode, hnode, onode, lr):
        # Ustawianie zmiennych lokalnych
        self.inode = inode
        self.hnode = hnode
        self.onode = onode
        self.lr = lr

        # Œrednia jest odwrotnoœci¹ pierwiastka sumy wêz³ów
        mean = 1/(pow((inode + hnode + onode), 0.5))

        # Odchylenie standardowe wynosi oko³o 1/6 ca³ego zakresu
        # Zakres = 2
        sd = 2/6

        # Generowanie obu macierzy wag
        # Macierz od warstwy wejœciowej do ukrytej
        self.wtgih = np.random.normal(mean, sd, [hnode, inode])

        # Macierz od warstwy ukrytej do wyjœciowej
        self.wtgho = np.random.normal(mean, sd, [onode, hnode])

    def testNet(self, input):
        # Konwersja wektora danych wejœciowych na tablicê numpy
        input = np.array(input, ndmin=2).T

        # Mno¿enie wejœcia przez wtgih
        hInput = np.dot(self.wtgih, input)

        # Stosowanie funkcji aktywacji
        hOutput = 1/(1 + np.exp(-hInput))

        # Mno¿enie wyjœcia warstwy ukrytej przez wtgho
        oInput = np.dot(self.wtgho, hOutput)

        # Stosowanie funkcji aktywacji
        oOutput = 1/(1 + np.exp(-oInput))
        return oOutput

    def trainNet(self, inputT, train):
        # Ten modu³ zale¿y od wartoœci, tablic i macierzy
        # utworzonych przy uruchamianiu modu³u init

        # Tworzenie tablic z argumentów
        self.inputT = np.array(inputT, ndmin=2).T
        self.train = np.array(train, ndmin=2).T

        # Mno¿enie tablicy inputT przez wtgih
        self.hInputT = np.dot(self.wtgih, self.inputT)

        # Stosowanie funkcji aktywacji
        self.hOutputT = 1/(1 + np.exp(-self.hInputT))

        # Mno¿enie wyjœcia warstwy ukrytej przez wtgho
        self.oInputT = np.dot(self.wtgho, self.hOutputT)

        # Stosowanie funkcji aktywacji
        self.oOutputT = 1/(1 + np.exp(-self.oInputT))

        # Obliczanie b³êdów wyjœcia
        self.eOutput = self.train - self.oOutputT

        # Obliczanie tablicy b³êdów warstwy ukrytej
        self.hError = np.dot(self.wtgho.T, self.eOutput)

        # Aktualizacja macierzy wag wtgho

        self.wtgho += self.lr*np.dot((self.eOutput*self.oOutputT*(1 - self.oOutputT)), self.hOutputT.T)

        # Aktualizacja macierzy wag wtgih
        self.wtgih += self.lr*np.dot((self.hError*self.hOutputT*(1 - self.hOutputT)), self.inputT.T)
