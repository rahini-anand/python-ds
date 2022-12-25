#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :363
Created on Fri Dec  9 12:11:16 2022
Title: perform slicing in 5*5 data frame
@author: rahini
"""
import numpy as np
import pandas as pd
r = [1001, 1002, 1003, 1004, 1005]
m = np.random.randint(60, 100, (5, 5))
s = ['Tamil', 'English', 'Maths', 'Science', 'Social']
f = pd.DataFrame(m, index=r, columns=s)

# first 2 rows and first 3 columns
f1 = f.loc[:1002, :'Maths']
print(f1)

# first 2 rows last 3 columns
f2 = f.loc[:1002, 'Maths':]
print(f2)

# middle 3 rows first 3 columns
f3 = f.loc[1002:1004, :'Maths']
print(f3)

# middle 3 rows last 3 columns
f4 = f.loc[1002:1004, 'Maths':]
print(f4)

# last two rows first 3 columns
f5 = f.loc[1004:, :'Maths']
print(f5)

# last 2 rows last 2 columns
f6 = f.loc[1004:, 'Science':]
print(f6)
