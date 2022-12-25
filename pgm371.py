#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :371
Created on Wed Dec 14 12:12:36 2022
Title: delete columns
@author: rahini
"""
import pandas as pd
import numpy as np
r = [1001, 1002, 1003, 1004, 1005]
m = np.random.randint(60, 100, (5, 5))
s = ['Tamil', 'English', 'Maths', 'Science', 'Social']
f = pd.DataFrame(m, index=r, columns=s)
#del function
del f['Tamil']
print(f)

# drop method
x1 = f.drop(['English', 'Maths'], axis=1)
print(f)
print(x1)

# pop method
x2 = f.pop('Science')
print(x2)

# drop (indexing) method
x3 = f.drop(f.columns[2], axis=1)
print(x3)
print(f)
