#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :211
Created on Thu Aug  4 12:30:11 2022
Title: display only alternative lines of the file
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
for i in range(0, l, 2):
    sp = a[i][1]
    f.seek(sp)
    x = f.readline()
    print(x)
