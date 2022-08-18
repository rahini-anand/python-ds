#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :209
Created on Wed Aug  3 12:27:57 2022
Title: display nth line
@author: rahini
"""
f = open('test.txt', 'r')
l = 1
sp = 0
a = []
for i in f:
    n = len(i)
    b = [l, sp, n, i]
    a.append(b)
    l += 1
    sp += n
for i in range(l-1):
    print(a[i][0], a[i][1], a[i][2], a[i][3])
nl = int(input('nl='))
nlsp = a[nl-1][1]
f.seek(nlsp)
x = f.readline()
print(x)
