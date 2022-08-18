#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :151
Created on Sun Jul 24 14:13:28 2022
Title: interchange second biggest and second
smallest no of n random no using function
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
print("small,big", small, big)
sbig = a[0]
ssmall = big
ssp = 0
sbp = 0
for i in range(n):
    if(a[i] > sbig and a[i] != big):
        sbig = a[i]
        sbp = i
    if(a[i] < ssmall and a[i] != small):
        ssmall = a[i]
        ssp = i
print("ssmall,sbig", ssmall, sbig)
y = a[sbp]
a[sbp] = a[ssp]
a[ssp] = y
for i in a:
    print(i)
