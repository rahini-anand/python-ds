#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :315
Created on Sat Oct 29 11:51:35 2022
Title: to sort and reverse the array
@author: rahini
"""
import numpy as np
f = open('50s marksheet copy.dat', 'rb')
a = np.fromfile("f", dtype=np.int64)
print(a)

# 1 sort an array
s = np.sort(a)
print(s)

# 2 reverse an array
r = np.flip(a)
print(r)
f.close()
