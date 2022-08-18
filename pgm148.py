#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :148
Created on Sun Jul 24 13:48:22 2022
Title: construct a list of n random nos and
        find its sum
@author: rahini
"""
n = int(input('n='))
a = []
for i in range(n):
    import random
    x = random.randint(0, 1000)
    a.append(x)
print(a)
ad = 0
for i in range(n):
    ad += a[i]
print(ad)
