#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :208
Created on Wed Aug  3 12:14:42 2022
Title: print starting point(offset) of eacg line
of file
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
    sp += n+1
print(a)
for i in range(l-1):
    print(a[i][0], a[i][1], a[i][2])
