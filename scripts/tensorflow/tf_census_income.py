"""
tensorflow and census income data
"""

from os.path import expanduser
import joblib

import tensorflow as tf

X_train, X_test, y_train, y_test = joblib.load(
    expanduser('~/Github/aimlds/data/clean/census_income.pkl')
    )

model_selu = tf.keras.Sequential([
    tf.keras.layers.Input(shape=X_train.shape[1:]),
    tf.keras.layers.Dense(1000, activation='selu', kernel_initializer='lecun_normal'),
    tf.keras.layers.Dense(1, activation='sigmoid')
    ])

model_selu.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

history_selu = model_selu.fit(X_train, y_train, epochs=15, validation_split=0.2)
