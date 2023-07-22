"""
Clean 'Census Income' dataset
"""

from os.path import expanduser
import pandas as pd

income_path = expanduser('~/Github/aimlds/data/raw/census_income/adult.data')
col_names = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 
 'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss',
 'hours_per_week', 'native_country', 'income_cat']

income_raw = pd.read_csv(income_path, names=col_names)

income_raw.to_csv('~/Github/aimlds/data/processed/census_income.csv')