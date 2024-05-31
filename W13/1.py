# Importowanie wymaganych bibliotek
import numpy as np
import matplotlib.pyplot as plt
from ANN import ANN
# Ustalenie konfiguracji sieci ANN
inode = 784
hnode = 100
onode = 10
# Ustawienie współczynnika uczenia
lr = 0.2
# Utworzenie wystąpienia obiektu ANN o nazwie ann
ann = ANN(inode, hnode, onode, lr)
# Utworzenie listy danych uczących
dataFile = open('mnist_train_100.csv')
dataList = dataFile.readlines()
dataFile.close()
# Uczenie ANN przy użyciu wszystkich rekordów z listy
for record in dataList:
    recordx = record.split(',')
    inputT = (np.asfarray(recordx[1:])/255.0*0.99) + 0.01
    train = np.zeros(onode) + 0.01
    train[int(recordx[0])] = 0.99
    # Uczenie zaczyna się tutaj
    ann.trainNet(inputT, train)
