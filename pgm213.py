#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :213
Created on Mon Aug  8 12:17:47 2022
Title: to write 'reverse the file o/p' in another
file
@author: rahini
"""
f1 = open('test.txt', 'r')
a = []
l = 1
sp = 0
for i in f1:
    n = len(i)
    b = [l, sp, n, i]
    a.append(b)
    sp += n
    l += 1
f2 = open('rtest.txt', 'w')
for i in range(1, l):
    sp = a[-i][1]
    f1.seek(sp)
    x = f1.readline()
    y = f2.write(x)
f1.close()
f2.close()
