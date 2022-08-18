#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :150R
Created on Sun Jul 24 14:05:36 2022
Title: interchange big and small of n random  no 
using function & method
@author: rahini
"""
a = []
n = int(input('n='))
for i in range(n):
    import random
    x = random.randint(0, 100)
    a.append(x)
print(a)
big = max(a)
small = min(a)
bp = a.index(big)
sp = a.index(small)
y = a[bp]
a[bp] = a[sp]
a[sp] = y
for i in a:
    print(i)
