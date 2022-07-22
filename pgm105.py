#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :105
Created on Mon Jul 18 16:17:33 2022
Title: Find transpose of 3*3 matrix
@author: rahini
"""
a = []
i = 0
while(i < 3):
    b = []
    j = 0
    while(j < 3):
        x = int(input('x='))
        b.append(x)
        j += 1
    a.append(b)
    i += 1
i = 0
while(i < 3):
    j = 0
    while(j < 3):
        print(a[j][i])
        j += 1
    i += 1
