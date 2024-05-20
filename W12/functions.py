# autorzy: Iga Bernat, Mikołaj Roszczyk
# data: 29 lutego 2024
# przedmiot: Metody Analizy Danych, laboratorium


import csv
import os
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import time
from math import sqrt
from scipy.interpolate import interp1d

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

def prepare_for_graph(data, no, scale):
    start_time = time.time()
    data_x=[]
    data_y=[]
    for row in data:
        data_x.append(row[3])
        data_y.append(row[no]*scale)
    print(f"czas przetwarzania danych do wykresu: {(time.time()-start_time)*1000}ms")
    return [data_x, data_y, scale]

def create_graph(data):
    plt.xlabel("czas[jednostka niepodana]")
    plt.ylabel("napięcie[V]")
    start_time = time.time()
    x = np.array(data[0])
    y = np.array(data[1])
    graph = plt.plot(x, y, ".")
    print(f"czas tworzenia wykresu: {(time.time()-start_time)/1000}ms")
    plt.show()
    return graph

def make_np_array(data, i):
    ch=[]
    for row in data:
        ch.append([row[i]])
    ch=np.array(ch)
    return ch

def test_train_divide(data, prop):
    train = []
    test = []
    for row in data:
        if np.random.rand() > prop:
            train.append(row)
        else:
            test.append(row)
    return train,  test
