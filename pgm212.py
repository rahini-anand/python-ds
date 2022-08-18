#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :212
Created on Mon Aug  8 11:39:21 2022
Title: display file in reverse order
@author: rahini
"""
f = open('test.txt', 'r')
a = []
l = 1
sp = 0
for i in f:
    n = len(i)
    b = [l, sp, n, i]
    a.append(b)
    sp += n
    l += 1
print(a)
for i in range(1, l):
    sp = a[-i][1]
    f.seek(sp)
    x = f.readline()
    print(x)
