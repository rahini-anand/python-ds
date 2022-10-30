#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :313
Created on Fri Oct 28 12:14:24 2022
Title: find out whether particular value present 
in an array and find out whether all values
in arrya satisfying the condition
@author: rahini
"""
import numpy as np
f = open('50s marksheet copy.dat', 'rb')
a = np.fromfile("f", dtype=np.int64)
print(a)

# 1 particular value
x = np.any(a == 50)
print(x)

# 2 All value
y = np.all(a < 100)
print(y)
