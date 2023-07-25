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
for col in income_raw.columns:
    if income_raw[col].dtype == 'object':
        income_raw[[col]] = income_raw[[col]].apply(lambda sr: sr.str.strip()) 

income_raw.to_csv('~/Github/aimlds/data/processed/census_income_raw.csv')

## feature engineering
def workclass_map(string):
    if string in ['Private']:
        return 'private'
    elif string in ['Local-gov', 'State-gov', 'Federal-gov']:
        return 'government'
    elif string in ['Self-emp-not-inc', 'Self-emp-inc']:
        return 'self_employed'
    elif string in ['?', 'Without-pay', 'Never-worked']:
        return 'other'

def education_map(string):
    if string in ['10th', '11th','12th','1st-4th','5th-6th', '7th-8th', '9th', 'Preschool']:
        return 'less_than_hs'
    elif string in ['HS-grad', 'Some-college']:
        return 'hs'
    elif string in ['Assoc-acdm', 'Assoc-voc', 'Bachelors', 'Prof-school']:
        return 'college'
    elif string in ['Masters', 'Doctorate']:
        return 'advanced'
    
def marital_map(string):
    if string in ['Married-civ-spouse', 'Married-spouse-absent', 'Married-AF-spouse']:
        return 'married'
    elif string in ['Never-married']:
        return 'never_married'
    elif string in ['Divorced', 'Separated', 'Widowed']:
        return 'no_longer_married'


def relationship_map(string):
    if string in ['Not-in-family', 'Own-child', 'Unmarried', 'Other-relative']:
        return 'other'
    else:
        return string.lower()

def race_map(string):
    if string == 'Asian-Pac-Islander':
        return 'aapi'
    elif string == 'Amer-Indian-Eskimo':
        return 'native_american'
    else:
        return string.lower()

income_mapped = income_raw.copy()
income_mapped['workclass'] = income_mapped['workclass'].map(workclass_map)
income_mapped['education'] = income_mapped['education'].map(education_map)
income_mapped['marital_status'] = income_mapped['marital_status'].map(marital_map)
income_mapped['relationship'] = income_mapped['relationship'].map(relationship_map)
income_mapped['race'] = income_mapped['race'].map(race_map)
income_mapped['sex'] = income_mapped['sex'].map(lambda s: s.lower())
income_mapped['filed_capital'] = ((income_mapped['capital_gain'] > 0) | (income_mapped['capital_loss'] > 0)).astype('int64')

col_keep = ['age', 'workclass', 'education', 'marital_status', 'relationship', 
            'race', 'sex', 'filed_capital', 'hours_per_week', 'income_cat']

income_cleaned = income_mapped[col_keep]
income_cleaned.to_csv('~/Github/aimlds/data/processed/census_income_cleaned.csv')






