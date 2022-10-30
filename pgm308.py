#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :308
Created on Fri Oct 21 12:22:16 2022
Title: print only positive nos from the array 
obtained from file using boolean array
@author: rahini
"""
import numpy as np
f = open('randomno.dat', 'rb')
a = np.fromfile("f", dtype=np.int64)
b = a >= 0
print(a[b])
