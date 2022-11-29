#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :331
Created on Thu Nov 10 11:41:39 2022
Title: perform vector operations in two matrices
@author: rahini
"""
import numpy as np
a = np.random.randint(0, 5, (5, 5))
b = np.random.randint(0, 5, (5, 5))
x = a.reshape(5, 5)
y = b.reshape(5, 5)
print(x)
print(y)
# 1 addition
ad = np.add(x, y)
print(ad)
# 2. subtraction
s = np.subtract(x, y)
print(s)
# 3. multiplicaiton
m = np.dot(x, y)
print(m)
