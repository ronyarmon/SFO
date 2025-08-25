import pandas as pd
import numpy as np
dcols = ['age', 'gender', 'income']
ds = pd.read_excel('/home/ronya/SFO/data/dataset.xlsx')[['year']+dcols]
years = np.arange(2010, 2018)
for c in dcols:
    print(f'*** {c} ***')
    for y in years:
        yds = ds[ds['year'] == y]
        print(f'{y}:', list(yds[c].unique()))