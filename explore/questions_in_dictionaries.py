import collections, re
import numpy as np
dicts_texts = np.load('demography/dicts_texts.npy', allow_pickle=True)[()]

# Scrape questions with codes from dictionaries
years_qlines = {}
for year, lines in dicts_texts.items():
    #print(f'*** {year} ***')
    lines = [l for l in lines if len(re.findall('^Q\d+', l))>0]
    year_dict = {}
    for line in lines:
        if len(re.findall('^Q\d+\w+', line))>0:
            name = re.findall('^Q\d+\w+', line)[0]
        question = line.replace(name, '').lstrip().rstrip()
        year_dict[name] = question
    years_qlines[year] = year_dict
years_qlines = collections.OrderedDict(sorted(years_qlines.items()))

# # Print to explore results to identify demographic and other questions by codes that were not collected yet
# print(30 * '*')
# print("questions dictionary")
# for year, questions in years_qlines.items():
#     print(30 * '*')
#     print(f'year {year} questions:')
#     for code, question in questions.items():
#         print(code, question)

# Which of the codes identified for questions that were not collected appear in which data dictionaries?
qcodes = ['SAFE', 'GETRATE', 'FIND', 'PROBLEM']
# codes for demographic questions
dcodes = ['Age', 'Gender', 'Household Income', 'FLY']

print(30 * '*')
print("questions dictionary")
dcodes_questions = {}
for year, questions in years_qlines.items():
    print(30 * '*')
    print(f'year {year} questions:')
    for code, question in questions.items():
        if (any(y in code for y in dcodes) | any(y in question for y in dcodes)):
            print(code, question)