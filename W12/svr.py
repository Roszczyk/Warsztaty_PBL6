from functions import read_csv_file, make_np_array
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import matplotlib.pyplot as plt
import time

from pathlib import Path
import os

os.chdir(Path(__file__).parent)

def run(x_data, y_data, name, degree, gamma, coef, tol, c, epsilon, shrinking):
    X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, random_state=1)
    for data in [X_train, X_test, y_train, y_test]:
        data = data.reshape(-1,1)
    scaler = preprocessing.StandardScaler().fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    begin_time = time.time()

    svr_reg = SVR(degree=degree, gamma=gamma, coef0=coef, tol=tol, C=c, epsilon=epsilon, shrinking=shrinking)

    svr_reg.fit(X_train, y_train)
    y_pred = svr_reg.predict(X_test)

    end_time = time.time()

    print(f"\n\n{name}\n")
    print(f"R2 SCORE: {round(r2_score(y_test, y_pred),2)}")
    print(f"Mean Squared Error: {round(mean_squared_error(y_test, y_pred), 2)}")
    print(f"Time: {end_time-begin_time} s")
    print("\n\n")



data, increment = read_csv_file("F_2_8_5b_NewFile4.csv")

ch1=make_np_array(data,0)*1000
ch2=make_np_array(data,1) *1000
ch3=make_np_array(data,2) *1000
times=make_np_array(data,3) *1000000

run(times, ch1, "CH1", c=10.0, coef=0.0, degree=2, epsilon=0.01, gamma='auto', shrinking=True, tol=0.0001)
run(times, ch2, "CH2", c=10.0, coef=0.0, degree=2, epsilon=0.2, gamma='scale', shrinking=True, tol=0.01)
run(times, ch3, "CH3", c=1.0, coef=0.0, degree=2, epsilon=0.2, gamma='auto', shrinking=True, tol=0.01)
