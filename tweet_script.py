import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import os

years = (1937, 2020)
year_range = range(years[0], years[1]+1)
datapath = './data'
unsorted_files = os.listdir(datapath)
files = sorted(unsorted_files)

data_m = pd.DataFrame()
data_f = pd.DataFrame()

for filename in files:
    if (filename == 'NationalReadMe.pdf'): continue

    year = filename[3:7]
    if (int(year) < years[0]) or (int(year) > years[1]):
        print(f'skipped {year}')
        continue

    data_m.at[year, '_length_lump'] = 0
    data_m.at[year, '_sum'] = 0

    data_f.at[year, '_length_lump'] = 0
    data_f.at[year, '_sum'] = 0

    print(f'examining names in {year}...')
    f = open(os.path.join(datapath, filename), 'r')
    for line in f:
        name_data_t = line.strip().split(',')
        name, number = (name_data_t[0], int(name_data_t[2]))
        if name_data_t[1] == 'M':
            data_m.at[year, name] = number
            data_m.at[year, '_length_lump'] += len(name) * number
            data_m.at[year, '_sum'] += number
        else:
            data_f.at[year, name] = number
            data_f.at[year, '_length_lump'] += len(name) * number
            data_f.at[year, '_sum'] += number
    f.close()

data_m['_avg_length'] = data_m['_length_lump'] / data_m['_sum']
data_m = data_m.sort_index(axis=1)

data_f['_avg_length'] = data_f['_length_lump'] / data_f['_sum']
data_f = data_f.sort_index(axis=1)

plt.plot(year_range, data_m['_avg_length'], label='M')
plt.plot(year_range, data_f['_avg_length'], label='F')
plt.legend(loc='upper left')
plt.xlabel('Year')
plt.ylabel('Average first name length (letters)')
plt.show()
