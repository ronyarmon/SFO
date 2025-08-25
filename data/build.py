import collections, os, re
import numpy as np
import pandas as pd

# Survey questions and codes collected from data dictionaries (using scripts and manually)
dicts_questions = {}
dicts_questions['2010'] = """Q6A Artwork and exhibitions
Q6B Restaurants
Q6C Retail shops and concessions
Q6D Signs and directions inside SFO
Q6E Escalators/Elevators/Moving walkways
Q6F Information on screens/monitors
Q6G Information booths (lower level - near baggage claim)
Q6H Information booths (upper level - departure area)
Q6I Signs and directions on SFO airport roadways
Q6J Airport parking facilities
Q6K AirTrain
Q6L Long term parking lot shuttle (bus ride)
Q6M Airport Rental Car Center
Q6N SFO Airport as a whole
Q17 Age
Q18 Gender
Q19 Income""".split('\n')

dicts_questions['2011'] = dicts_questions['2012'] = """Q8A Artwork and exhibitions
Q8B Restaurants
Q8C Retail shops and concessions
Q8D Signs and directions inside SFO
Q8E Escalators/Elevators/Moving walkways
Q8F Information on screens/monitors
Q8G Information booths (lower level - near baggage claim)
Q8H Information booths (upper level - departure area)
Q8I Signs and directions on SFO airport roadways
Q8J Airport parking facilities
Q8K AirTrain
Q8L Long term parking lot shuttle (bus ride)
Q8M Airport Rental Car Center
Q8N SFO Airport as a whole
Q19 Age
Q20 Gender
Q21 Income""".split('\n')

dicts_questions['2012'] = """Q8A_ART Artwork and exhibitions
Q8B_FOOD Restaurants
Q8C_SHOP Retail shops and concessions
Q8D_SIGNS Signs and directions inside SFO
Q8E_WALK Escalators/Elevators/Moving walkways
Q8F_SCREENS Information on screens/monitors
Q8G_INFOARR Information booths (lower level - near baggage claim)
Q8H_INFODEP Information booths (upper level - departure area)
Q8I_ROAD Signs and directions on SFO airport roadways
Q8J_PARK Airport parking facilities
Q8K_AIRTRAIN AirTrain
Q8L_LTPARK Long term parking lot shuttle (bus ride)
Q8M_RENTAL Airport Rental Car Center
Q8N_WHOLE SFO Airport as a whole
Q19_AGE Age
Q20_SEX Gender
Q21_INCOME Income""".split('\n')

dicts_questions['2013'] = """Q7A_ART Artwork and exhibitions
Q7B_FOOD Restaurants
Q7C_SHOPS Retail shops and concessions
Q7D_SIGNS Signs and directions inside SFO
Q7E_WALK Escalators/Elevators/Moving walkways
Q7F_SCREENS Information on screens/monitors
Q7G_INFOARR Information booths (lower level - near baggage claim)
Q7H_INFODEP Information booths (upper level - departure area)
Q7I_WIFI Accessing and using free WiFi at SFO
Q7J_ROAD Signs and directions on SFO airport roadways
Q7K_PARK  Airport parking facilities
Q7L_AIRTRAIN AirTrain
Q7M_LTPARK Long term parking lot shuttle (bus ride)
Q7N_RENTAL Airport Rental Car Center
Q7O_WHOLE SFO Airport as a whole
Q18_AGE Age
Q19_SEX Gender
Q20_INCOME Income
""".split('\n')

dicts_questions['2014'] = dicts_questions['2015'] = """Q7ART Artwork and exhibitions
Q7FOOD Restaurants
Q7STORE Retail shops and concessions
Q7SIGN Signs and directions inside SFO
Q7WALKWAYS Escalators/Elevators/Moving walkways
Q7SCREENS Information on screens/monitors
Q7INFODOWN Information booths (lower level - near baggage claim)
Q7INFOUP Information booths (upper level - departure area)
Q7WIFI Accessing and using free WiFi at SFO
Q7ROADS Signs and directions on SFO airport roadways
Q7PARK  Airport parking facilities
Q7AIRTRAIN AirTrain
Q7LTPARKING Long term parking lot shuttle (bus ride)
Q7RENTAL Airport Rental Car Center
Q7ALL SFO Airport as a whole
Q18AGE Age
Q19GENDER Gender
Q20INCOME Income""".split('\n')

dicts_questions['2016'] = """Q7ART Artwork and exhibitions
Q7FOOD Restaurants
Q7STORE Retail shops and concessions
Q7SIGN Signs and directions inside SFO
Q7WALKWAYS Escalators/Elevators/Moving walkways
Q7SCREENS Information on screens/monitors
Q7INFODOWN Information booths (lower level - near baggage claim)
Q7INFOUP Information booths (upper level - departure area)
Q7WIFI Accessing and using free WiFi at SFO
Q7ROADS Signs and directions on SFO airport roadways
Q7PARK  Airport parking facilities
Q7AIRTRAIN AirTrain
Q7LTPARKING Long term parking lot shuttle (bus ride)
Q7RENTAL Airport Rental Car Center
Q7ALL SFO Airport as a whole
Q19AGE Age
Q20GENDER Gender
Q21INCME Income""".split('\n')

dicts_questions['2017'] = """Q7ART Artwork and exhibitions
Q7FOOD Restaurants
Q7STORE Retail shops and concessions
Q7SIGN Signs and directions inside SFO
Q7WALKWAYS Escalators/Elevators/Moving walkways
Q7SCREENS Information on screens/monitors
Q7INFODOWN Information booths (lower level - near baggage claim)
Q7INFOUP Information booths (upper level - departure area)
Q7WIFI Accessing and using free WiFi at SFO
Q7ROADS Signs and directions on SFO airport roadways
Q7PARK  Airport parking facilities
Q7AIRTRAIN AirTrain
Q7LTPARKING Long term parking lot shuttle (bus ride)
Q7RENTAL Airport Rental Car Center
Q7ALL SFO Airport as a whole
Q19AGE Age
Q20GENDER Gender
Q21INCOME Income""".split('\n')

dicts_questions['2018'] = """Q7ART Artwork and exhibitions
Q7FOOD Restaurants
Q7STORE Retail shops and concessions
Q7SIGN Signs and directions inside SFO
Q7WALKWAY Escalators/Elevators/Moving walkways
Q7SCREENS Information on screens/monitors
Q7INFODOWN Information booths (lower level - near baggage claim)
Q7INFOUP Information booths (upper level - departure area)
Q7WIFI Accessing and using free WiFi at SFO
Q7ROADS Signs and directions on SFO airport roadways
Q7PARK  Airport parking facilities
Q7AIRTRAIN AirTrain
Q7LTPARKING Long term parking lot shuttle (bus ride)
Q7RENTAL Airport Rental Car Center
Q7ALL SFO Airport as a whole
Q20Age Age
Q21Gender Gender
Q22Income Income
""".split('\n')

dicts_questions = collections.OrderedDict(sorted(dicts_questions.items()))
# Standard questions with their standard names
questions_names = {'Artwork and exhibitions': 'ART', 'Restaurants': 'FOOD', 'Retail shops and concessions': 'STORE',\
                   'Signs and directions inside SFO': 'SIGN', 'Escalators/Elevators/Moving walkways': 'WALKWAYS',\
                   'Information on screens/monitors': 'SCREENS', 'Information booths (lower level - near baggage claim)': 'INFODOWN',\
                   'Information booths (upper level - departure area)': 'INFOUP', 'Accessing and using free WiFi at SFO': 'WIFI',\
                   'Signs and directions on SFO airport roadways': 'ROADS', 'Airport parking facilities': 'PARK', 'AirTrain': 'AIRTRAIN',\
                   'Long term parking lot shuttle (bus ride)': 'LTPARKING', 'Airport Rental Car Center': 'RENTAL',\
                   'SFO Airport as a whole': 'ALL', 'Age':'Age', 'Gender': 'Gender', 'Income': 'Income'}
questions = list(questions_names.keys())
# Store the normalized name for each column of each year's dataset
names_norm = {}
for year, lines in dicts_questions.items():
    print(f'*** {year} ***')
    lines = [l for l in lines if ((any(y in l for y in questions) & (len(re.findall('^Q\d{1,}', l))>0)))]
    yquestions = []
    year_dict = {}
    for line in lines:
        print(line)
        name = re.findall('^Q\d+\w+', line)[0]
        question = line.replace(name, '').lstrip().rstrip()
        if question in questions:
            year_dict[name] = questions_names[question]
            yquestions.append(question) # tracking
        else: print(f'question - {question} not in questions')
    print(f'{len(set(yquestions))} questions identified in dictionary')
    diff = set(questions).difference(set(yquestions))
    if diff: print(f'{len(diff)} questions missing: {diff}')
    names_norm[year] = year_dict
print(30 * '*')
print("questions dictionary")
for k,v in names_norm.items(): print(k, len(v), v)


dcols = ['Age', 'Gender', 'Income']
data_path = '/home/ronya/SFO/data'
raw_path = os.path.join(data_path, 'raw')
files = os.listdir(raw_path)
dfs = {}
for file in files:
    year = re.findall('^201\d', file)[0]
    year_names_norm = names_norm[year]
    df = pd.read_csv(os.path.join(raw_path, file))
    names = list(year_names_norm.keys())
    cols = [c for c in df.columns if c in names]
    df = df[cols].rename(columns=year_names_norm)
    # print(f'{year} demography value counts at source files renamed')
    # for c in dcols:
    #     vc = df[c].value_counts().sort_index()
    #     print(f'column {c}, counts:\n', vc)
    #     n = 1
    if 'WIFI' not in df.columns: df['WIFI'] = 0
    df['year'] = int(year)
    dfs[file] = df
dfs = pd.concat(list(dfs.values()), axis=0, ignore_index=True)
print(dfs.info())
dfs.to_excel(os.path.join(data_path, 'merged.xlsx'), index=False)