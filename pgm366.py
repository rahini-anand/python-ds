#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :366
Created on Tue Dec 13 12:03:07 2022
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

# first 2 rows
f1 = f.iloc[:2, ]
print(f1)

# middle 3 rows
f2 = f.iloc[1:4, ]
print(f2)

# last 2 rows
f3 = f.iloc[3:, ]
print(f3)

# alternate rows
f4 = f.iloc[::2, ]
