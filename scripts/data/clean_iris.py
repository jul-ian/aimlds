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

