#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :
Created on Tue Dec 13 12:20:40 2022
Title: 
@author: rahini
"""
import numpy as np
import pandas as pd
r = [1001, 1002, 1003, 1004, 1005]
m = np.random.randint(60, 100, (5, 5))
s = ['Tamil', 'English', 'Maths', 'Science', 'Social']
f = pd.DataFrame(m, index=r, columns=s)
print(f)

# first two columns
f1 = f.iloc[::, :2]
print(f1)

# middle 3 columns
f2 = f.iloc[::, 1:4]
print(f2)

# last 2 columns
f3 = f.iloc[::, 3:]
print(f3)

# alternate columns
f4 = f.iloc[::, ::2]
print(f4)
