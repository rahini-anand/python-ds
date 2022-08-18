#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :207
Created on Wed Aug  3 11:57:06 2022
Title: store the starting point, line no,length
of line and text in a list
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
