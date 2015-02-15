# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 23:18:32 2015

@author: runkyo
"""

import datetime
import pandas as pd
from pandas.io.data import DataReader
import matplotlib
import matplotlib.pyplot as plt

start = datetime.datetime(2014, 1, 1)
end = datetime.datetime(2015, 2, 15)

df = DataReader("005930.KS", "yahoo", start, end)

df['MA_5'] = pd.stats.moments.rolling_mean(df['Adj Close'], 5)
df['MA_20'] = pd.stats.moments.rolling_mean(df['Adj Close'], 20)
df['diff'] = df['MA_5'] - df['MA_20']


#df.head(10)


prev_key = prev_val = 0

for key, val in df['diff'][1:].iteritems():
    if val == 0:
        continue
    if val * prev_val < 0 and val > prev_val:
        print '[golden]', key, val
    if val * prev_val < 0 and val < prev_val:
        print '[dead]', key, val
    prev_key, prev_val = key, val
    

ax = df[['Adj Close', 'MA_5', 'MA_20']].plot(figsize=(16,6))
prev_key = prev_val = 0

for key, val in df['diff'][1:].iteritems():
    if val == 0:
        continue

    if val * prev_val < 0 and val > prev_val:
        ax.annotate('Golden', xy=(key, df['MA_20'][key]), xytext=(10,-30), textcoords='offset points', arrowprops=dict(arrowstyle='-|>'))
    if val * prev_val < 0 and val < prev_val:
        ax.annotate('Dead', xy=(key, df['MA_20'][key]), xytext=(10,30), textcoords='offset points', arrowprops=dict(arrowstyle='-|>'))
        
    prev_key, prev_val = key, val    
    
    
    
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(16, 18)

# price (가격)
price_chart = plt.subplot2grid((4,1), (0, 0), rowspan=2)
price_chart.plot(df.index, df['Adj Close'], label='Adj Close')
price_chart.plot(df.index, df['MA_5'], label='MA 5day')
price_chart.plot(df.index, df['MA_20'], label='MA 20day')

plt.title(u'Samsung')
plt.legend(loc='best')

# volume (거래량)
vol_chart = plt.subplot2grid((4,1), (2,0), rowspan=1)
vol_chart.bar(df.index, df['Volume'], color='c')

# 이동평균의 차이
signal_chart = plt.subplot2grid((4,1), (3,0), rowspan=1)
signal_chart.plot(df.index, df['diff'].fillna(0), color='g')
plt.axhline(y=0, linestyle='--', color='k')

# sell, buy annotate
prev_key = prev_val = 0

for key, val in df['diff'][1:].iteritems():
    if val == 0:
        continue
    if val * prev_val < 0 and val > prev_val:
        signal_chart.annotate('Buy', xy=(key, df['diff'][key]), xytext=(10,-30), textcoords='offset points', arrowprops=dict(arrowstyle='-|>'))
    if val * prev_val < 0 and val < prev_val:
        signal_chart.annotate('Sell', xy=(key, df['diff'][key]), xytext=(10,30), textcoords='offset points', arrowprops=dict(arrowstyle='-|>'))
    prev_key, prev_val = key, val
    
    