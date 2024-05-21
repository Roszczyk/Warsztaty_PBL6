# autorzy: Iga Bernat, Mikołaj Roszczyk
# data: 29 lutego 2024
# przedmiot: Metody Analizy Danych, laboratorium


import csv
import numpy as np

def read_csv_file(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the first header row
        header2 = next(csv_reader)  # Skip the second header row
        increment = float(header2[5])
        start = float(header2[4])
        for row in csv_reader:
            points = [0,0,0,0]
            points[0]=float(row[1])
            points[1]=float(row[2])
            points[2]=float(row[3])
            points[3]=start # zakładamy, że pierwsza próbka została pobrana w czasie startu
            start=start+increment     # a kolejne co wartość increment
            data.append(points)
    return data,increment


def make_np_array(data, i):
    ch=[]
    for row in data:
        ch.append([row[i]])
    ch=np.array(ch)
    return ch