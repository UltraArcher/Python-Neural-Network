import tensorflow as tf
import keras
from keras import layers
from keras.layers import Activation, Dense
import numpy as np

X = np.array(([0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]), dtype=float)
y = np.array(([1], [0], [0], [0], [0], [0], [0], [1]), dtype=float)

model = keras.Sequential()
model.add(Dense(4, input_dim=3, activation="relu", use_bias=True))
model.add(Dense(1, activation="sigmoid", use_bias=True))

model.compile(loss="mean_squared_error", optimizer="adam", metrics=["binary_accuracy"])

print(model.get_weights())

history = model.fit(X, y, epochs=2000, validation_data=(X, y))

model.summary()

loss_history = history.history["loss"]
numpy_loss_history = np.array(loss_history)
np.savetxt("loss_history.txt", numpy_loss_history, delimiter="\n")
binary_accuracy_history = history.history["binary_accuracy"]
numpy_binary_accuracy = np.array(binary_accuracy_history)
np.savetxt("binary_accuracy.txt", numpy_binary_accuracy, delimiter="\n")

print(np.mean(history.history["binary_accuracy"]))
result = model.predict(X ).round()
print(result)