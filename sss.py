# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 01:28:36 2015

@author: runkyo

http://sencha.tistory.com/attachment/cfile25.uf@234C8C3853A12B3724E709.pdf
http://sencha.tistory.com/attachment/cfile27.uf@2250FC3853A12B3619CA32.pdf

"""

import numpy as np
import pandas as pd
from pandas import DataFrame, Series


# Series Object
s1 = Series(range(0,4))
s2 = Series(range(1,5))
s3 = s1 + s2
s4 = Series(['a','b']) *3

#DataFrame Ojbect

trivial = Series(range(1,6))
statePop	=	Series({'NSW':6917658,	
				'Vic':5354042,	'Qld':4332739,
				'WA':	2239170,	'SA':1596572})
stateArea	=	Series({'NSW':800642,	
				'Vic':227416,	'Qld':1730648,
				'WA':	2529875,	'SA':983482}) #	in	km**2
    
    
pop_in_millions	=	statePop	/	1000000
state_pop_density	=	statePop	/	stateArea

large	=	statePop	[statePop	>= 5000000]