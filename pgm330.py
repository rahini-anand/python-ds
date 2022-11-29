#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :330
Created on Wed Nov  9 12:24:32 2022
Title: to perform scalar operations in two dimensional
array
@author: rahini
"""
import numpy as np
a = np.random.randint(0, 20, (5, 5))
x = a.reshape(5, 5)
print(x)
# 1.addition
ad = x+10
print(ad)
# 2. subraction
s = x-10
print(s)
# 3.multiplication
m = x*10
print(m)
# 4. division
d = x/10
print(d)
# 5.remainder
r = x % 2
print(r)
# 6.quotient
q = x//2
print(q)
