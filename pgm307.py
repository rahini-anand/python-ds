#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :307
Created on Fri Oct 21 12:15:31 2022
Title: to get positive nos from array(boolean 
array)
@author: rahini
"""
import numpy as np
f = open('randomno.dat', 'rb')
a = np.fromfile("f", dtype=np.int64)
b = a >= 0
print(b)
