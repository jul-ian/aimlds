"""
Script to clean the iris dataset for use
"""

from datadir import datadir
from os.path import join
import pandas as pd

irispath = join(datadir, 'raw/iris.data')
names_iris = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris_raw = pd.read_csv(irispath, names=names_iris)

iris_raw.to_csv(join(datadir, 'processed/iris.csv'))

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MaxMinScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

num_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
cat_cols = ['species']

num_pipeline = Pipeline([
    ('scaler', MinMaxScaler())
    ])
cat_pipeline = Pipeline([
    ('encoder', LabelEncoder())
    ])

full_pipeline = ColumnTransformer([
    ('num', num_pipeline, num_cols),
    ('cat', cat_pipeline, cat_cols)
    ])
iris_clean = full_pipeline.fit_transform()