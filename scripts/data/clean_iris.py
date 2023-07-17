"""
Script to clean the iris dataset for use
"""

import pandas as pd
import joblib
from os.path import expanduser

names_iris = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris_raw = pd.read_csv('~/Github/aimlds/data/raw/iris.data', names=names_iris)

iris_raw.to_csv('~/Github/aimlds/data/processed/iris.csv')

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

iris_train, iris_test = train_test_split(iris_raw, test_size=0.2)

features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
target = ['species']

X_train, X_test = iris_train[features].to_numpy(), iris_test[features].to_numpy()
y_train, y_test = iris_train[target].to_numpy(), iris_test[target].to_numpy()

encoder = LabelEncoder()
scaler = MinMaxScaler()

X_train, y_train = scaler.fit_transform(X_train), encoder.fit_transform(y_train.ravel())
X_test, y_test = scaler.transform(X_test), encoder.transform(y_test.ravel())

joblib.dump((X_train, X_test, y_train, y_test), 
            expanduser('~/Github/aimlds/data/clean/irisxy_train_test.pkl'))



