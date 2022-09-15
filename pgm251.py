#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :251
Created on Tue Sep  6 12:47:32 2022
Title: find difference of two matrices using 
lambda funciton
@author: rahini
"""
import random
def m(n): return [[random.randint(0, 10) for j in range(n)]for i in range(n)]
def d(a, b): return [[a[i][j]-b[i][j]for j in range(3)]for i in range(3)]


# main
m1 = m(3)
m2 = m(3)
diff = d(m1, m2)
print(m1)
print(m2)
print(diff)
