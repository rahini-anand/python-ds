#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :309
Created on Sat Oct 22 11:41:40 2022
Title: to segregate single,two and three digit
using boolean array
@author: rahini
"""
import numpy as np
f = open('randomno.dat', 'rb')
a = np.fromfile("f", dtype=np.int64)
b1 = (a >= 0) & (a <= 9)
b2 = (a >= 10) & (a <= 99)
b3 = (a >= 100) & (a <= 999)
print(a[b1])
print(a[b2])
print(a[b3])
