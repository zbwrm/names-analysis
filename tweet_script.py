import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib as plt
import os

years = (1999, 2005)
datapath = './data'
unsorted_files = os.listdir(datapath)
files = sorted(unsorted_files)

data_m = pd.DataFrame()
data_f = pd.DataFrame()
data_m_l = pd.DataFrame()
data_f_l = pd.DataFrame()

for filename in files:
    if (filename == 'NationalReadMe.pdf'): continue

    year = int(filename[3:7])
    if (year < years[0]) or (year > years[1]):
        print(f'skipped {year}')
        continue

    print(f'examining names in {year}...')
    f = open(os.path.join(datapath, filename), 'r')
    for line in f:
        name_data_t = line.strip().split(',')
        name, number = (name_data_t[0], name_data_t[2])
        # print(f' - {name_data_t[0]}: {name_data_t[2]}')
        if name_data_t[1] == 'M':
            data_m.at[name, year] = rumber
            data_m.at[name, 'length'] = name.length
            data_m_l.at['avg_helper', year] += name.length * number
        else:
            data_f.at[name, year] = number
            data_f_l.at[name.length, year] += number
    f.close()

# data_m_l.loc['average'] = data_m_l[' / 
sns.set_theme(style='dark')

print(data_m.head())
