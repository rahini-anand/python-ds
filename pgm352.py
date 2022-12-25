#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :352
Created on Wed Nov 30 11:48:54 2022
Title: calculating final marks from end,mid semester
and attendence, assignment
@author: rahini
"""
import pandas as pd
r1 = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
m = [70, 50, 40, 52, 67, 74, 57, 88, 41, 77]
r2 = [1008, 1005, 1001, 1007, 1003, 1010, 1002, 1004, 1006, 1009]
e = [71, 64, 55, 88, 91, 76, 54, 67, 78, 71]
r3 = [1009, 1007, 1005, 1003, 1001, 1002, 1004, 1006, 1008, 1010]
a = [7, 8, 9, 7, 8, 6, 8, 9, 8, 7]
r4 = [1010, 1008, 1006, 1004, 1002, 1009, 1007, 1005, 1003, 1001]
at = [5, 4, 4, 4, 5, 4, 5, 4, 4, 5]
s1 = pd.Series(m, index=r1)
s2 = pd.Series(e, index=r2)
s3 = pd.Series(a, index=r3)
s4 = pd.Series(at, index=r4)
c1 = s1/100*40
c2 = s2/100*45
f = c1+c2+s3+s4
print(f)
