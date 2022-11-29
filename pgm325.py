#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :325
Created on Sat Nov  5 12:14:23 2022
Title: read matrix from file and print it row by
row
@author: rahini
"""
import numpy as np
f = open('matrix.dat', 'rb')
a = np.fromfile("f", dtype=np.int64)
x = a.reshape(5, 5)
print(x)
r1 = x[0:1:, ]
print(r1)
r2 = x[1:2:, ]
print(r2)
r3 = x[2:3:, ]
print(r3)
r4 = x[3:4:, ]
print(r4)
r5 = x[4:5:, ]
print(r5)
f.close()
