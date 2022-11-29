#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :326
Created on Tue Nov  8 11:56:47 2022
Title: print matrix column by column
@author: rahini
"""
import numpy as np
f = open('matrix.dat', 'rb')
a = np.fromfile("f", dtype=np.int64)
x = a.reshape(5, 5)
c1 = x[:, 0:1]
c2 = x[:, 1:2]
c3 = x[:, 2:3]
c4 = x[:, 3:4]
c5 = x[:, 4:5]
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
f.close()
