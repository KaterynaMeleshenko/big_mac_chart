import numpy as np
import pandas as pd

big_mac_price = pd.read_csv('big-mac-source-data.csv')

# Leave the freshest data
big_mac_price = big_mac_price[big_mac_price['date'] == '2024-01-01']

# Find the max GDP among countries for further normalization
max_GDP = big_mac_price['GDP_dollar'].max() # as to 01.01.2024 it is Norway

# Calculate BigMac prices in usd
big_mac_price['big_mac_doll'] = round(big_mac_price['local_price'] / big_mac_price['dollar_ex'], 2)

# Carry normalization for BigMac prices 
big_mac_price['adj_doll'] = round(big_mac_price['big_mac_doll'] * max_GDP / big_mac_price['GDP_dollar'], 2)