import numpy as np
import tflite_runtime.interpreter as tflite

x_test = []
# Wczytaj dane MNIST
for i in range(5):
    x_test.append(np.random.rand(28,28))
x_test = np.array(x_test)

# Wczytaj model TFLite
interpreter = tflite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

# Pobierz dane wejściowe i wyjściowe
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Przeprowadź inferencję na wybranych obrazkach
for i, img in enumerate(x_test):
    img = np.expand_dims(img, axis=0)  # Dodaj wymiar batch
    interpreter.set_tensor(input_details[0]['index'], img)
    interpreter.invoke()
    
    # Odczytaj wynik inferencji
    output_data = interpreter.get_tensor(output_details[0]['index'])
    predicted_label = np.argmax(output_data)
    print(f"Obrazek {i+1}, Predykcja: {predicted_label}")