#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :193
Created on Thu Jul 28 21:10:01 2022
Title: to count the frequency of nos in list and
store the values and count in a list
@author: rahini
"""
import random
n = int(input('n='))
a = [random.randint(0, 100) for x in range(n)]
s = set(a)
print(a)
print(s)
m = []
for i in s:
    counts = a.count(i)
    values = i
    b = [counts, values]
    m.append(b)
print(m)
