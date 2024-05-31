import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras import utils
import tensorflow.lite as tflite

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

def save_tflite_model(model, filename):
    converter = tflite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()
    print(tflite_model)
    with open(filename, "wb") as f:
        f.write(tflite_model)


if __name__ == "__main__":
    X_train, y_train, X_test, y_test, num_pixels = init_data()
    num_classes = y_test.shape[1]
    model = baseline_model(num_pixels, num_classes)
    model.fit(X_train, y_train, validation_data = (X_test, y_test), epochs = 10, batch_size = 200, verbose = 2)
    scores = model.evaluate(X_test, y_test, verbose = 0)
    print(f"\n\nBaseline error: {round(100-scores[1]*100, 4)}\n\n")
    model.save('model.h5')
    # save_tflite_model(model, 'model.tflite')

# import numpy as np
# from keras.datasets import mnist
# from keras.models import Sequential
# from keras.layers import Dense
# from keras import utils
# import tensorflow as tf

# seed = 42
# np.random.seed(seed)

# def init_data():
#     (X_train, y_train), (X_test, y_test) = mnist.load_data()
#     num_pixels = X_train.shape[1] * X_train.shape[2]
#     X_train = X_train.reshape(X_train.shape[0], num_pixels).astype('float32')
#     X_test = X_test.reshape(X_test.shape[0], num_pixels).astype('float32')
#     X_train = X_train / 255.0
#     X_test = X_test / 255.0
#     y_train = utils.to_categorical(y_train)
#     y_test = utils.to_categorical(y_test)
#     return X_train, y_train, X_test, y_test, num_pixels

# def baseline_model(num_pixels, num_classes):
#     model = Sequential()
#     model.add(Dense(num_pixels, input_dim=num_pixels, kernel_initializer='normal', activation='relu'))
#     model.add(Dense(num_classes, kernel_initializer='normal', activation='softmax'))
#     model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#     return model

# def save_tflite_model(model, filename):
#     try:
#         print("Starting conversion to TFLite model...")
#         converter = tf.lite.TFLiteConverter.from_keras_model(model)
#         tflite_model = converter.convert()
#         print("Conversion successful, saving model...")
#         with open(filename, "wb") as f:
#             f.write(tflite_model)
#         print(f"Model saved to {filename}")
#     except Exception as e:
#         print(f"Error during model conversion or saving: {e}")

# if __name__ == "__main__":
#     X_train, y_train, X_test, y_test, num_pixels = init_data()
#     num_classes = y_test.shape[1]
#     model = baseline_model(num_pixels, num_classes)
#     model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=200, verbose=2)
#     scores = model.evaluate(X_test, y_test, verbose=0)
#     print(f"\n\nBaseline error: {round(100 - scores[1] * 100, 4)}\n\n")
#     save_tflite_model(model, 'model.tflite')
