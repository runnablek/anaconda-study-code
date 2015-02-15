# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 22:42:19 2015

@author: runkyo
"""

import pandas as pd

fn = 'data/krx_sector.json'
df = pd.read_json(fn)
df.head()