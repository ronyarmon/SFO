import re
import numpy as np
vals = [v.lstrip().rstrip() for v in open('demographic_values_2018.txt').read().split('\n') if v]
dicts_texts = np.load('dicts_texts.npy', allow_pickle=True)[()]
a = 0
years = np.arange(2010, 2018)
for val in vals:
    vyears = []
    for year, lines in dicts_texts.items():
        for line in lines:
            if len(re.findall(val, line))>0:
                #print(year, line)
                vyears.append(int(year))
    diff = set(years).difference(set(vyears))
    if diff:
        diff = list(diff).sort()
        print(f'{val} is missing from:', diff)


