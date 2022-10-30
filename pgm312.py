#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :312
Created on Fri Oct 28 11:53:34 2022
Title: to perform vector operations in an array
@author: rahini
"""
import numpy as np
import random
f = open('50s marksheet copy.dat', 'rb')
a = np.fromfile("f", dtype=np.int64)
bl = [random.randint(0, 100) for x in range(50)]
b = np.array(bl)
print(a)
print(b)

# 1 Addition
aa = [a[i]+b[i] for i in range(50)]
print(aa)

# 2 subraction
sa = [a[i]-b[i] for i in range(50)]
print(sa)

# 3 Multiplication
ma = [a[i]*b[i] for i in range(50)]
print(ma)

# 4 Division
da = [a[i]/b[i] for i in range(50)]
print(da)

# 5 Remainder
ra = [a[i] % b[i] for i in range(50)]
print(ra)

# 6 Quotient
qa = [a[i]//b[i] for i in range(50)]
print(qa)

f.close()
