#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :156
Created on Mon Jul 25 00:12:55 2022
Title: sum of two 3*3 matrix
@author: rahini
"""
a = []
for i in range(3):
    b = []
    for j in range(3):
        x = int(input('x='))
        b.append(x)
    a.append(b)
c = []
for i in range(3):
    d = []
    for j in range(3):
        y = int(input('y='))
        d.append(y)
    c.append(d)
e = []
for i in range(3):
    f = []
    for j in range(3):
        ad = a[i][j]+c[i][j]
        f.append(ad)
    e.append(f)
print(e)
