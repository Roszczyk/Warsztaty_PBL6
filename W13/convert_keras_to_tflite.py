# import keras
# import tensorflow as tf
import os
from pathlib import Path

os.chdir(Path(__file__).parent)

# model = keras.models.load_model('model.h5')
# model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

# print("Keras model loaded")

# converter = tf.lite.TFLiteConverter.from_keras_model(model)
# converter.experimental_new_converter = True
# converter.allow_custom_ops = True

# tflite_model = converter.convert()

# with tf.io.gfile.GFile('model.tflite', 'wb') as f:
#   f.write(tflite_model)

import tensorflow as tf

def convert_keras_to_tf(keras_model, saved_model_path):
    tf.saved_model.save(keras_model, saved_model_path)
    print(f"Model TensorFlow saved at {saved_model_path}")

model = tf.keras.models.load_model('model.h5')
# converter = tf.lite.TFLiteConverter.from_keras_model(model)
# tflite_model = converter.convert()

convert_keras_to_tf(model, "saved_model")

converter = tf.lite.TFLiteConverter.from_saved_model("saved_model")
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)