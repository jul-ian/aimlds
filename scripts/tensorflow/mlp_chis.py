"""

Using tensorflow with CHIS data

"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import tensorflow as tf
from tensorflow.keras import layers

adult_2019 = pd.read_pickle('~/Github/aimlds/data/processed/adult_2019.pkl')
adult_2020 = pd.read_pickle('~/Github/aimlds/data/processed/adult_2020.pkl')

adult_1920 = pd.concat([adult_2019, adult_2020], axis=0)

features = ['srsex', 'srage_p1', 'ahedc_p1', 'ombsrr_p1', 'marit2', 'ur_clrt6', 'wrkst_p1']
target = ['ab1']

adult = adult_1920[features + target]
adult = adult.assign(ab1 = lambda df: df[target[0]] - 1)
adult_train, adult_test = train_test_split(adult, test_size=0.2)

encoder = OneHotEncoder(sparse=False)
X_train = encoder.fit_transform(adult_train[features])
X_test = encoder.transform(adult_test[features])
y_train = adult_train[target].to_numpy(dtype='int64')
y_test = adult_test[target].to_numpy(dtype='int64')


mlp_model = tf.keras.Sequential([
    layers.Dense(512, activation='relu', input_shape=X_train.shape[1:]),
    layers.Dense(256, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(5, activation='softmax')
    ])
mlp_model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
mlp_model.fit(X_train, y_train, epochs=30, validation_split=0.2)




