#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :324
Created on Sat Nov  5 11:51:54 2022
Title: to read matrix from file and display it
@author: rahini
"""
import numpy as np
f = open('matrix.dat', 'rb')
a = np.fromfile("f", dtype=np.int64)
x = a.reshape(5, 5)
print(x)
f.close()
