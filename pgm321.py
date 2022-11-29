#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :321
Created on Fri Nov  4 11:51:41 2022
Title: construct numpy array of two dimensional 5*5 
matrix and print it element by element
@author: rahini
"""
import numpy as np
a = np.random.randint(0, 20, (5, 5))
print(a)
for i in range(5):
    for j in range(5):
        print(a[i][j], end=' ')
    print()
