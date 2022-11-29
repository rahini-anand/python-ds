#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :319
Created on Thu Nov  3 12:06:44 2022
Title: to apply np mehtods on n students marks
@author: rahini
"""
import numpy as np
import random
sl = [random.randint(0, 100) for i in range(50)]
s = np.array(sl)
print(s)

# 1 Max mark
f = s.max()
print(f)

# 2 Min mark
l = s.min()
print(l)

# 3 sort
a = np.sort(s)
print(a)

# 4 unique marks,index and count
u, i, c = np.unique(s, return_index=True, return_counts=True)
print(u, i, c)
