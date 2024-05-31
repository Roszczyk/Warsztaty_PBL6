import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras import utils

seed = 42
np.random.seed(seed)

def init_data():
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    num_pixels = X_train.shape[1] * X_train.shape[2]
    X_train = X_train.reshape(X_train.shape[0], num_pixels).astype('float32')
    X_test = X_test.reshape(X_test.shape[0], num_pixels).astype('float32')
    X_train = X_train / 255.0
    X_test = X_test / 255.0
    y_train = utils.to_categorical(y_train)
    y_test = utils.to_categorical(y_test)
    return X_train, y_train, X_test, y_test, num_pixels

def baseline_model(num_pixels, num_classes):
    model = Sequential()
    model.add(Dense(num_pixels, input_dim = num_pixels, kernel_initializer='normal', activation = 'relu'))
    model.add(Dense(num_classes, kernel_initializer = 'normal', activation = 'softmax'))
    model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
    return model


if __name__ == "__main__":
    X_train, y_train, X_test, y_test, num_pixels = init_data()
    num_classes = y_test.shape[1]
    model = baseline_model(num_pixels, num_classes)
    model.fit(X_train, y_train, validation_data = (X_test, y_test), epochs = 10, batch_size = 200, verbose = 2)
    scores = model.evaluate(X_test, y_test, verbose = 0)
    print(f"Baseline error: {round(100-scores[1]*100, 4)}")