#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :101
Created on Mon Jul 18 15:51:01 2022
Title: Interchange the second biggest and second
        smallest number
@author: rahini
"""
a = []
i = 0
while(i < 10):
    x = int(input('x='))
    a.append(x)
    i += 1
big = a[0]
small = a[0]
i = 0
while(i < 10):
    big = a[i] if a[i] > big else big
    small = a[i] if a[i] < small else small
    i += 1
sbig = small
ssmall = big
sbp = 0
ssp = 0
i = 0
while(i < 10):
    if(a[i] > sbig and a[i] != big):
        sbig = a[i]
        sbp = i
    if(a[i] < ssmall and a[i] != small):
        ssmall = a[i]
        ssp = i
    i += 1
y = a[sbp]
a[sbp] = a[ssp]
a[ssp] = y
i = 0
print(big, small)
print(sbig, ssmall)
while(i < 10):
    print(a[i])
    i += 1
