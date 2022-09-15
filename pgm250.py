#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :250
Created on Tue Sep  6 12:40:14 2022
Title: find sum of two matrices using lambda
function
@author: rahini
"""
import random
def m(n): return [[random.randint(0, 10) for j in range(n)]for i in range(n)]
def s(a, b): return [[a[i][j]+b[i][j]for j in range(3)]for i in range(3)]


# main
m1 = m(3)
m2 = m(3)
sums = s(m1, m2)
print(m1)
print(m2)
print(sums)
