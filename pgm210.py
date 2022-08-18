#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :210
Created on Thu Aug  4 12:10:48 2022
Title: display mth line to nth line
@author: rahini
"""
f = open('test.txt', 'r')
l = 1
a = []
sp = 0
for i in f:
    n = len(i)
    b = [l, sp, n, i]
    a.append(b)
    sp += n
    l += 1
print(a)
ml = int(input('ml='))
nl = int(input('nl='))
for i in range(ml-1, nl+1):
    sp = a[i][1]
    f.seek(sp)
    x = f.readline()
    print(x)
