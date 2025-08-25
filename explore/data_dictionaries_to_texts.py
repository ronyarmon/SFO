import os, re
import numpy as np
from pypdf import PdfReader
dict_path = '/home/ronya/SFO/data/dictionaries'
files = [f for f in os.listdir(dict_path) if f.endswith('.pdf')]
# creating a pdf reader object

def pdf_file_text(fpath):
    '''
    Extract the text of a pdf file
    :param fpath (str): path to a pdf file
    :return: text of the pdf file in fpath
    '''
    reader = PdfReader(fpath)
    file_text = ''
    for i in range(len(reader.pages)): file_text += reader.pages[i] .extract_text()
    return file_text
dicts_texts = {}
for i, file in enumerate(files):
    dicts_texts[re.findall('201\d', file)[0]] =\
    pdf_file_text(os.path.join(dict_path, files[i])).split('\n')
np.save('demography/dicts_texts.npy', dicts_texts)