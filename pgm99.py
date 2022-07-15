#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no : 99
Created on Thu Jul 14 13:48:51 2022
Title: interchange big and small no in a list of 10 int nos
@author: rahini
"""
a = []
i = 0
while(i < 10):
    x = int(input('x:'))
    a.append(x)
    i += 1
i = 0
big = a[0]
small = a[0]
bp = 0
sp = 0
while(i < 10):
    if(a[i] > big):
        big = a[i]
        bp = i
    if(a[i] < small):
        small = a[i]
        sp = i
    i += 1
y = a[bp]
a[bp] = a[sp]
a[sp] = y
print(sp, bp)
i = 0
while(i < 10):
    print(a[i])
    i += 1
