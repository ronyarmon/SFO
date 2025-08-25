import os
import pandas as pd
raw_path = '/data/raw'
files = os.listdir(raw_path)
file_cols = {}
for file in files:
    file_cols[file] = set(pd.read_csv(os.path.join(raw_path, file)).columns)
for file1, cols1 in file_cols.items():
    for file2, cols2 in file_cols.items():
        result_str = f'{file1} columns compared to {file2} columns: '
        diff = cols1.difference(cols2)
        if diff: result_str += f'differ in {diff}'
        else: result_str += 'identical'
        print(result_str)

    
    
    