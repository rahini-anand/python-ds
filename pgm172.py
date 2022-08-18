#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :172
Created on Mon Jul 25 14:57:48 2022
Title: construct 3*3 matrix using nested loop 
and find its transpose
@author: rahini
"""
import random
a = [[random.randint(0, 1000)
      for i in range(3)]
     for j in range(3)]
print(a)
t = [
    [a[i][j]
     for i in range(3)]
    for j in range(3)
]
print(t)
