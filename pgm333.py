#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :333
Created on Thu Nov 10 12:05:00 2022
Title: find out column and row total, column and
row maximum and minimum
@author: rahini
"""
import numpy as np
a = np.random.randint(0, 10, (5, 5))
x = a.reshape(5, 5)
print(x)
# 1.column total
ct = x.sum(axis=0)
print(ct)

# 2.row total
rt = x.sum(axis=1)
print(rt)

# 3 column maximum
cmax = x.max(axis=0)
print(cmax)

# 4 row maximum
rmax = x.max(axis=1)
print(rmax)

# 5 column minimum
cmin = x.min(axis=0)
print(cmin)

# 6 row minimum
rmin = x.min(axis=1)
print(rmin)
