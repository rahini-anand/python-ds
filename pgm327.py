#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :327
Created on Tue Nov  8 13:21:21 2022
Title: perform 12 types of slicing in matrix
@author: rahini
"""
import numpy as np
f = open('matrix.dat', 'rb')
a = np.fromfile("f", dtype=np.int64)
x = a.reshape(5, 5)
print(x)
# 1 first 2 rows
s1 = x[0:2, ]
print(s1)
# 2 middle 3 rows
s2 = x[1:4, ]
print(s2)
# 3 last 2 rows
s3 = x[3:5, ]
print(s3)
# 4 fist 2 columns
s4 = x[:, 0:2]
print(s4)
# 5 middle 3 columns
s5 = x[:, 1:4]
print(s5)
# 6 last 2 columns
s6 = x[:, 3:5]
print(s6)
# 7 first 2 rows first 3 columns
s7 = x[0:2, 0:3]
print(s7)
# 8 first 2 rows last 3 columns
s8 = x[0:2, 2:5]
print(s8)
# 9 second 2 rows first 3 columns
s9 = x[2:4, 0:3]
print(s9)
# 10 second 2 rows last 3 columns
s10 = x[2:4, 2:5]
print(s10)
# 11 last 2 rows first 3 columns
s11 = x[3:5, 0:3]
print(s11)
# 12 last 2 rows last 2 columns
s12 = x[3:5, 3:5]
print(s12)
f.close()
