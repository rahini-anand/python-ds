#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :357
Created on Tue Dec  6 12:06:09 2022
Title: remove NaN
@author: rahini
"""
import pandas as pd
r1 = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
m1 = [70, 50, 40, 52, 67, 74, 57, 88, 41, 77]
s1 = pd.Series(m1, index=r1)
r2 = [1008, 1005, 1001, 1007, 1003, 1010]
m2 = [71, 64, 55, 88, 91, 76]
s2 = pd.Series(m2, index=r2)


# sum of two series
s = s1+s2
print(s)

# Remove NaN
sr = s.dropna()
print(sr)
