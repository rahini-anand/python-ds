#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :318
Created on Thu Nov  3 11:47:18 2022
Title: to find out unique elements in array and find 
its index and count
@author: rahini
"""
import numpy as np
f = open('50s marksheet copy.dat', 'rb')
a = np.fromfile("f", dtype=np.int64)
print(a)
# 1 unique elements in array
u = np.unique(a)
print(u)

# 2 index of unique elements and count
a1, b, c = np.unique(a, return_index=True, return_counts=True)
print(a1, b, c)

f.close()
