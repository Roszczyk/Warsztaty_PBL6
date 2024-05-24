from functions import read_csv_file, make_np_array
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import time

from pathlib import Path
import os

os.chdir(Path(__file__).parent)

def run(x_data, y_data, name, alpha, normalize_y, optimizer):
    X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, random_state=1)
    for data in [X_train, X_test, y_train, y_test]:
        data = data.reshape(-1,1)
    scaler = preprocessing.StandardScaler().fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    begin_training = time.time()

    gpr_reg = GaussianProcessRegressor(alpha=alpha, normalize_y=normalize_y, optimizer=optimizer)
    gpr_reg.fit(X_train, y_train)

    end_training = time.time()

    begin_inference = time.time()
    y_pred = gpr_reg.predict(X_test)
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

run(times, ch1, "CH1", alpha = 1e-10, normalize_y = True, optimizer='fmin_l_bfgs_b')
run(times, ch2, "CH2", alpha = 1e-9, normalize_y = True, optimizer='fmin_l_bfgs_b')
run(times, ch3, "CH3", alpha = 1e-10, normalize_y = False, optimizer='fmin_l_bfgs_b')