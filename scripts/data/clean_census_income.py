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

## feature engineering
workclass_map = {
    'private': ['Private'],
    'government': ['Local-gove', 'State-gov', 'Federal-gov'],
    'self_employed': ['Self-emp-not-inc', 'Self-emp-inc'],
    'other': ['?', 'Without-pay', 'Never-worked']
    }
education_map = {
    'less_than_hs': ['10th', '11th','12th','1st-4th', 
                     '5th-6th', '7th-8th', '9th', 'Preschool'],
    'hs': ['HS-grad', 'Some-college'],
    'college': ['Assoc-acdm', 'Assoc-voc', 'Bachelors', 'Prof-school'],
    'advance_college': ['Masters', 'Doctorate']
    }
marital_map = {
    'married': ['Married-civ-spouse', 'Married-spouse-absent', 'Married-AF-spouse'],
    'never_married': ['Never-married'],
    'no_longer_married': ['Divorced', 'Separated', 'Widowed']
    }
relationship_map = {
    'husband': ['Husband'], 'wife': ['Wife'],
    'other': ['Not-in-family', 'Own-child', 'Unmarried', 'Other-relative']
    }

race_map = {
    'white': "White", "Black": 'black', 'other': 'Other',
    'aapi': 'Asian-Pac-Islander', 'native': 'Amer-Indian_Eskimo'
    }

income_mapped = income_raw.copy()
df1 = income_mapped.assign(workclass = income_mapped['workclass'].map(workclass_map))

