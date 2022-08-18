#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :214
Created on Tue Aug  9 12:00:41 2022
Title: store all the odd lines in one file and 
all the even lines in another file
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
    l += 1
    sp += n
f2 = open('odd.txt', 'w')
for i in range(0, l-1, 2):
    sp = a[i][1]
    f1.seek(sp)
    x = f1.readline()
    y = f2.write(x)
f3 = open('even.txt', 'w')
for i in range(1, l-1, 2):
    sp = a[i][1]
    f1.seek(sp)
    x = f1.readline()
    y = f3.write(x)
f1.close()
f2.close()
f3.close()
