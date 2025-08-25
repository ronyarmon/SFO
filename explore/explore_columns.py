import os
import pandas as pd
raw_path = '/data/raw'
files = ['2014_SFO_Customer_Survey_20250817.csv', '2017_SFO_Customer_Survey_20250817.csv']
for file in files:
    print(file)
    print(pd.read_csv(os.path.join(raw_path, file)).columns)