#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :303
Created on Wed Oct 19 11:57:20 2022
Title: to construct different types of array
@author: rahini
"""
import numpy as np
import random

# 1 zero array
a1 = np.zeros(10)
print(a1)

# 2 ones array
a2 = np.ones(10)
print(a2)

# 3 constant array
a3 = np.full(10, 999)
print(a3)

# 4 array with range of nos
a4 = np.arange(1, 6, 1)
print(a4)

# 5 array of random real nos
a5 = np.random.random(10)
print(a5)

# 6 normal distribution array
a6 = np.random.normal(0, 1, 10)
print(a6)

# 7 array of random int nos
a7 = np.random.randint(0, 100, 10)
print(a7)

# 8 empty array
a8 = np.empty(10)
print(a8)
