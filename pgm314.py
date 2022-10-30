#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :314
Created on Sat Oct 29 11:43:14 2022
Title: to find sum, maximum element and minimum element 
of the array
@author: rahini
"""
import numpy as np
f = open('50s marksheet copy.dat', 'rb')
a = np.fromfile("f", dtype=np.int64)
print(a)

# 1 sum of elements in array
s = a.sum()
print(s)

# 2 maximum element of array
maxi = a.max()
print(maxi)

# 3 minimum element of the array
mini = a.min()
print(mini)
