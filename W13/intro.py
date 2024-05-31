import numpy as np

# Importowanie wymaganych bibliotek
import matplotlib.pyplot as plt

# Tworzenie listy danych
dataFile = open('mnist/mnist_train_100.csv')
dataList = dataFile.readlines()
dataFile.close()

# Pobieranie numeru rekordu
print('Wprowadź numer rekordu do wyświetlenia: ', end=' ')
num = input()

# Pobieranie rekordu
record = dataList[int(num)].split(',')

# Zmiana kształtu tablicy w celu wizualizacji
imageArray = np.asfarray(record[1:]).reshape(28, 28)

# Wyświetlenie obrazu w skali szarości
plt.imshow(imageArray, cmap='Greys', interpolation='None')
plt.show()
