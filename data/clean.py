import os
import pandas as pd
import numpy as np
data_path = '/home/ronya/SFO/data'
dfs=pd.read_excel(os.path.join(data_path, 'merged.xlsx'))
# Data wrangling
dfs.columns = [c.lower() for c in dfs.columns]
dfs = dfs.replace(to_replace=['BLANK', 'Blank'], value=0)
# Replace numeric values in demography by responses
dem_dict = \
{'age':{1:'Under 18',2:'18 - 24',3:'25 - 34',4:'35 - 44', 5:'45 - 54',6:'55 - 64',7:'65 and over',0:'Blank', 8: 'Blank', 9: 'Blank',
'Under 20':'18 - 24', 'Under 23':'18 - 24', 'Under 25':'18 - 24', 'Under 27':'25 - 34', 'Under 28':'25 - 34', 'Under 30':'25 - 34',
        'Under 32':'25 - 34', 'Under 19':'18 - 24', 'Under 21':'18 - 24',
'Under 22':'18 - 24', 'Under 24':'18 - 24', 'Under 26':'25 - 34', 'Under 29':'25 - 34', 'Under 31':'25 - 34', "Don't Know or Refused": 'Blank'},
'gender':{1:'Male',2:'Female', 3:'Blank', 0:'Blank', '0':'Blank', 4: 'Blank', 'Other': 'Blank'},
'income':{1:'Under 50,000',2:'$50,000 - $100,000',\
           3:'$100,001 - $150,000',4:'Over $150,000', 0:'Blank', 5:'Blank', 6:'Blank', 'Other Currency':'Blank'}}
dcols = ['age', 'gender', 'income']
for c in dcols: dfs[c].replace(dem_dict[c], inplace=True)
dfs['age'].replace(to_replace='65 and over', value = '65-Over', inplace=True)
dfs.replace(to_replace='Blank/Multiple responses', value='Blank', inplace=True)
dfs.replace(to_replace=np.nan, value='Blank', inplace=True)
dfs.replace(to_replace='\s-\s', value='-', regex=True, inplace=True)
qcols = [c for c in dfs.columns if c not in dcols]
dfs[qcols] = dfs[qcols].fillna(0).astype(int)
for col in qcols:
    if col == 'year': dfs[col] = dfs[col].astype(pd.Int16Dtype())
    else: dfs[col] = dfs[col].astype(pd.Int8Dtype())
qcols.remove('year')
dfs = dfs[['year']+dcols+qcols]
dfs.to_excel(os.path.join(data_path, 'dataset.xlsx'), index=False)
print(dfs.info())