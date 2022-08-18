#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :121
Created on Sat Jul 23 14:32:26 2022
Title: count no of positive,negative and zero
    in n random nos
@author: rahini
"""
n = int(input('n='))
cp = 0
cn = 0
cz = 0
for i in range(n):
    import random
    x = random.randint(-1000, 1000)
    if(x > 0):
        cp += 1
    elif(x < 0):
        cn += 1
    else:
        cz += 1
    print(x)
print(cp, cn, cz)
