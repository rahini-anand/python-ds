#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :368
Created on Tue Dec 13 12:29:51 2022
Title: row and column combined slicing
@author: rahini
"""
import numpy as np
import pandas as pd
r = [1001, 1002, 1003, 1004, 1005]
m = np.random.randint(60, 100, (5, 5))
s = ['Tamil', 'English', 'Maths', 'Science', 'Social']
f = pd.DataFrame(m, index=r, columns=s)

# first 2 rows and first 3 columns
f1 = f.iloc[:2, :3]
print(f1)

# first 2 rows last 3 columns
f2 = f.iloc[:2, 2:]
print(f2)

# middle 3 rows first 3 columns
f3 = f.iloc[1:4, :3]
print(f3)

# middle 3 rows last 3 columns
f4 = f.iloc[1:4, 2:]
print(f4)

# last two rows first 3 columns
f5 = f.iloc[3:, :3]
print(f5)

# last 2 rows last 2 columns
f6 = f.iloc[3:, 3:]
print(f6)
