#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :317
Created on Sat Oct 29 12:15:45 2022
Title: to perform the following operation in an array
@author: rahini
"""
import numpy as np
import random
f = open('50s marksheet copy.dat', 'rb')
a = np.fromfile("f", dtype=np.int64)
print(a)
bl = [random.randint(0, 100) for i in range(50)]
b = np.array(bl)
print(b)

# 1. concatenate two array
x = np.concatenate([a, b])
print(x)

# 2 delete the element from array
y = np.delete(a, [10])
print(y)

# 3 insert the element from array
z = np.insert(a, 0, 5, axis=0)
print(z)

f.close()
