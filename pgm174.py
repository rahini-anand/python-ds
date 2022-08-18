#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :174
Created on Mon Jul 25 15:05:04 2022
Title: construct two 3*3 matrix using nested loop
and find its difference
@author: rahini
"""
import random
a = [[random.randint(0, 10)
     for j in range(3)]
     for i in range(3)]
print(a)
b = [[random.randint(0, 10)
     for j in range(3)]
     for i in range(3)]
print(b)
d = [[a[i][j]-b[i][j]
     for j in range(3)]
     for i in range(3)]
print(d)
