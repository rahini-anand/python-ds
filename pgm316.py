#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :316
Created on Sat Oct 29 12:04:12 2022
Title: to split the array by different methods
@author: rahini
"""

import numpy as np
f = open('50s marksheet copy.dat', 'rb')
a = np.fromfile("f", dtype=np.int64)
print(a)

# 1. split with single variable
x = np.split(a, 10)
print(x)

# 2 split with multiple variable
x1, x2, x3, x4, x5 = np.split(a, 5)
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)

# 3 split by choosing element
xn = np.split(a, [5, 15, 25])
print(xn)

f.close()
