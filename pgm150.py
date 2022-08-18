#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :150
Created on Sun Jul 24 13:58:57 2022
Title: interhchange the biggest and smallest 
element of n random no list
@author: rahini
"""
a = []
n = int(input('n='))
for i in range(n):
    import random
    x = random.randint(0, 1000)
    a.append(x)
print(a)
big = a[0]
small = a[0]
bp = 0
sp = 0
for i in range(n):
    if(a[i] > big):
        big = a[i]
        bp = i
    if(a[i] < small):
        small = a[i]
        sp = i
print(small, big)
y = a[bp]
a[bp] = a[sp]
a[sp] = y
for i in a:
    print(i)
