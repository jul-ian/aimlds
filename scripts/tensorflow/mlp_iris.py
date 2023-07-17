"""
tf using iris
"""

import joblib
from os.path import expanduser

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

iris_path = expanduser('~/Github/aimlds/data/clean/irisxy_train_test.pkl')
X_train, X_test, y_train, y_test = joblib.load(iris_path)

mlp_model = Sequential([
    Dense(64, activation='selu', input_shape=(4,)),
    Dense(64, activation='selu'),
    Dense(3, activation='softmax')
    ])

mlp_model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

mlp_model.fit(X_train, y_train, epochs=20, validation_split=0.1)