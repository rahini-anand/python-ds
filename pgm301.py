#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :301
Created on Tue Oct 18 12:08:23 2022
Title: count no of positive,negative and zeros
in a numpy array
@author: rahini
"""
import numpy as np
import random

cp = 0
cn = 0
cz = 0
l = [random.randint(-100, 100) for i in range(20)]
npl = np.array(l)
print(npl)
for i in range(20):
    if(npl[i] > 0):
        cp += 1
    elif(npl[i] < 0):
        cn += 1
    else:
        cz += 1

print(cp, cn, cz)
