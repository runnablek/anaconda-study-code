# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 22:58:41 2015

@author: runkyo
"""

import requests
import pandas as pd
from StringIO import StringIO

url = 'http://real-chart.finance.yahoo.com/table.csv?' \
        's=^KS11&a=0&b=1&c=2013&d=11&e=31&f=2013&g=d'

r = requests.get(url)
df = pd.read_csv(StringIO(r.content), index_col='Date', parse_dates={'Date'})


#df['Adj Close'].plot(figsize=(16, 4), title='KOSPI')
#df['Volume'].plot(figsize=(16, 4), style='g')


df2 =  df[['Adj Close', 'Volume']]
df2.head()
#df2['Adj Close'].plot(figsize=(16, 4), style='b')
#df2['Volume'].plot(figsize=(16, 4), style='g', secondary_y=True)


# 특정일 이후 부터 데이터만 조회하기...
df2['2013-07':]['Adj Close'].plot(figsize=(16, 4), style='b')
df2['2013-07':]['Volume'].plot(figsize=(16, 4), style='g', secondary_y=True)


#스캐터차트

df3 =  df[['Adj Close', 'Volume']]
df3.plot(y='Adj Close', x='Volume', style='o')


#Normalize
#시계열 데이터를 0~1 사이의 값으로 변환
#데이터의 변화를 상대적으로 비교

df_norm = (df2 - df2.mean()) / (df2.max() - df2.min())
df_norm.plot(figsize=(16, 4))


