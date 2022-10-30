#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :311
Created on Fri Oct 28 11:22:32 2022
Title: to perform scalar operations in an array
@author: rahini
"""
import numpy as np
f = open('50s marksheet copy.dat', 'rb')
a = np.fromfile("f", dtype=np.int64)
print(a)

# 1 Addition
aa = a+5
print(aa)

# 2 Subratction
sa = a-5
print(sa)

# 3 Multiplication
ma = a*2
print(ma)

# 4 Division
da = a/2
print(da)

# 5 Remainder
ra = a % 2
print(ra)

# 6 Quotient
qa = a//2
print(qa)

f.close()
