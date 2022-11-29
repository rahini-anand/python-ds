#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :322
Created on Fri Nov  4 12:26:21 2022
Title: find transpose of matrix
@author: rahini
"""
import numpy as np
a = np.random.randint(0, 20, (5, 5))
print(a)

# Transpose of a
for i in range(5):
    for j in range(5):
        print(a[j][i], end=' ')
    print()
