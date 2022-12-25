#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :365
Created on Tue Dec 13 11:50:59 2022
Title: column wise slicing
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
f1 = f.loc[::, :'English']
print(f1)

# middle 3 columns
f2 = f.loc[::, 'English':'Science']
print(f2)

# last 2 columns
f3 = f.loc[::, 'Science':]
print(f3)

# alternate columns
f4 = f.loc[::, ::2]
print(f4)
