#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :181
Created on Mon Jul 25 15:39:06 2022
Title: construct a tuple of n random nos and
count no of positive,negative and zero
@author: rahini
"""
import random
n = int(input('n='))
li = [random.randint(-1000, 1000) for x in range(n)]
a = (li)
print(a)
cp = 0
cn = 0
cz = 0
for i in range(n):
    if(a[i] > 0):
        cp += 1
    elif(a[i] < 0):
        cn += 1
    else:
        cz += 1
print(cp, cn, cz)
