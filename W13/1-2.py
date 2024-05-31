# Importowanie wymaganych bibliotek
import numpy as np
from ANN import ANN
# Ustalenie konfiguracji sieci ANN
inode = 784
hnode = 100
onode = 10

# Utworzenie listy danych uczących
dataFile = open('mnist_train_100.csv')
dataList = dataFile.readlines()
dataFile.close()
# Tworzenie listy danych testowych
testDataFile = open('mnist_test_10.csv')
testDataList = testDataFile.readlines()
testDataFile.close()


def train_and_test(lr):
    ann = ANN(inode, hnode, onode, lr)
    # Uczenie sieci ANN przy użyciu wszystkich rekordów z listy
    for record in dataList:
        recordx = record.split(',')
        inputT = (np.asfarray(recordx[1:])/255.0*0.99) + 0.01
        train = np.zeros(onode) + 0.01
        train[int(recordx[0])] = 0.99
        # Uczenie zaczyna się tutaj
        ann.trainNet(inputT, train)
    # Iteracja przez wszystkie rekordy testowe
    match = 0
    no_match = 0

    for record in testDataList:
        recordz = record.split(',')
        # Wyznaczenie etykiety rekordu
        labelz = int(recordz[0])
        # Dostosowanie wartości rekordów dla sieci ANN
        inputz = (np.asfarray(recordz[1:])/255.0*0.99)+0.01
        outputz = ann.testNet(inputz)
        max_value = np.argmax(outputz)
        if max_value == labelz:
            match = match + 1
        else:
            no_match = no_match + 1
        success = float(match) / float(match + no_match)
    # Wyświetlenie współczynnika uczenia i współczynnika sukcesu
    print('lr = {0:.1} success rate = {1}'.format(lr, success))


for i in range(10):
    print('\nIteracja: ', i + 1)
    for lr in np.arange(0.1, 0.6, 0.1):
        train_and_test(lr)
