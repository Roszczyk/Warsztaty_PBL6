from functions import read_csv_file, make_np_array
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import time

from pathlib import Path
import os

os.chdir(Path(__file__).parent)

def run(x_data, y_data, name, criterion, splitter, max_depth, min_samples_split):
    X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, random_state=1)
    for data in [X_train, X_test, y_train, y_test]:
        data = data.reshape(-1,1)
    scaler = preprocessing.StandardScaler().fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    begin_training = time.time()

    cart_reg = DecisionTreeRegressor(criterion=criterion, splitter=splitter, max_depth=max_depth, min_samples_split=min_samples_split)
    cart_reg.fit(X_train, y_train)

    end_training = time.time()

    begin_inference = time.time()
    y_pred = cart_reg.predict(X_test)
    end_inference = time.time()

    print(f"\n\n{name}\n")
    print(f"R2 SCORE: {round(r2_score(y_test, y_pred),2)}")
    print(f"Mean Squared Error: {round(mean_squared_error(y_test, y_pred), 2)}")
    print(f"Time TRAINING: {1000*(end_training-begin_training)} ms")
    print(f"Time INFERENCE: {1000*(end_inference - begin_inference)} ms")
    print("\n\n")

data, increment = read_csv_file("F_2_8_5b_NewFile4.csv")

ch1=make_np_array(data,0)*1000
ch2=make_np_array(data,1) *1000
ch3=make_np_array(data,2) *1000
times=make_np_array(data,3) *1000000

run(times, ch1, "CH1", criterion='friedman_mse', splitter='random', max_depth=15, min_samples_split=3)
run(times, ch2, "CH2", criterion='friedman_mse', splitter='best', max_depth=15, min_samples_split=5)
run(times, ch3, "CH3", criterion='squared_error', splitter='best', max_depth=15, min_samples_split=5)