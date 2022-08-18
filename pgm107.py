#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :107
Created on Fri Jul 22 14:39:07 2022
Title: product of two matrices
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
        k = 0
        p = 0
        while(k < 3):
            p = p+a[i][k]*c[k][j]
            k += 1
        f.append(p)
        j += 1
    e.append(f)
    i += 1
print(e)
