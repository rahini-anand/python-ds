#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :194
Created on Mon Aug  1 12:26:52 2022
Title: find the highest and lowest occurence n
no in the list
@author: rahini
"""
import random
n = int(input('n='))
a = [random.randint(0, 100) for x in range(n)]
s = set(a)
print(a)
print(s)
m = []
t = 0
for i in s:
    counts = a.count(i)
    values = i
    t += 1
    b = [counts, values]
    m.append(b)
print(m)
ho = m[0][0]
hov = m[0][1]
lo = m[0][0]
lov = m[0][1]
for i in range(t):
    if(m[i][0] > ho):
        ho = m[i][0]
        hov = m[i][1]
    if(m[i][0] < lo):
        lo = m[i][0]
        lov = m[i][1]
print(lov, hov)
