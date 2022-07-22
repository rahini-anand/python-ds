#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :106
Created on Mon Jul 18 16:22:27 2022
Title: find the sum of two 3*3 matrix
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
c = []
i = 0
while(i < 3):
    d = []
    j = 0
    while(j < 3):
        y = int(input('y='))
        d.append(y)
        j += 1
    c.append(d)
    i += 1
e = []
i = 0
while(i < 3):
    f = []
    j = 0
    while(j < 3):
        s = a[i][j]+b[i][j]
        f.append(s)
        j += 1
    e.append(f)
    i += 1
print(e)
