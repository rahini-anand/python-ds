#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :334
Created on Thu Nov 10 12:24:35 2022
Title: to save matrix in text file and load 
the matrix from text file and display it
@author: rahini
"""
import numpy as np
a = np.random.randint(0, 10, (5, 5))
x = a.reshape(5, 5)
print(x)

# save matrix in text file
np.savetxt("matrix.txt", x)

# load matrix from text file
y = np.loadtxt("matrix.txt", dtype=np.int32)
print(y)
