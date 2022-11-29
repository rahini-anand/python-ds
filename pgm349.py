#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :349
Created on Sat Nov 26 12:20:55 2022
Title: to change elements in series
@author: rahini
"""
import pandas as pd

r = [i for i in range(1001, 1021)]
m1 = [35, 67, 45, 78, 45, 23, 54, 73, 92, 82,
      71, 61, 63, 21, 76, 90, 30, 41, 50, 65]
m2 = [90, 70, 38, 50, 55, 68, 34, 53, 71, 66,
      42, 98, 81, 38, 46, 77, 39, 55, 88, 90]
p1 = pd.Series(m1, index=r)
p2 = pd.Series(m2, index=r)
print(p1)
print(p2)

p1[1010] = 100
p1[1015] = 0
p2[1010] = 100
p2[1015] = 0
print(p1)
print(p2)
