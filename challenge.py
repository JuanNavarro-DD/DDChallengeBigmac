''' 
Juan Navarro
Data diver

This file reads the data from
https://github.com/TheEconomist/big-mac-data/tree/master/output-data
big-mac-full-index.csv

'''

import pandas as pd


url = 'https://raw.githubusercontent.com/TheEconomist/big-mac-data/master/output-data/big-mac-full-index.csv'
data = pd.read_csv(url, index_col=1)

print(data)