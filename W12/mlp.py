from functions import read_csv_file, make_np_array
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import time

from pathlib import Path
import os

os.chdir(Path(__file__).parent)

def run(x_data, y_data, name, activation, alpha, hls, lr, max_iter, solver):
    X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, random_state=1)
    for data in [X_train, X_test, y_train, y_test]:
        data = data.reshape(-1,1)
    scaler = preprocessing.StandardScaler().fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    begin_time = time.time()

    mlp_reg = MLPRegressor(activation=activation, alpha=alpha, hidden_layer_sizes=hls, learning_rate=lr, max_iter=max_iter, solver=solver)
    mlp_reg.fit(X_train, y_train)
    y_pred = mlp_reg.predict(X_test)

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

run(times, ch1, "CH1", activation='tanh', alpha=0.0001, hls=(15, 20), lr='constant', max_iter=100, solver='lbfgs')
run(times, ch2, "CH2", activation='relu', alpha=0.0001, hls=(20,15), lr='invscaling', max_iter=100, solver='lbfgs')
run(times, ch3, "CH3", activation='tanh', alpha=0.05, hls=(15,20), lr='adaptive', max_iter=100, solver='lbfgs')