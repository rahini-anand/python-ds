#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :206
Created on Tue Aug  2 12:03:36 2022
Title: display the highest occurence of the words
of line
@author: rahini
"""
f = open('test.txt', 'r')
l = 1
a = []
for i in f:
    w = i.split()
    cw = len(w)
    nc = len(i)
    b = [l, cw, i]
    a.append(b)
    l += 1
ho = a[0][1]
hol = a[0][0]
hoi = a[0][2]
for i in range(l-1):
    if(a[i][1] > ho):
        ho = a[i][1]
        hol = a[i][0]
        hoi = a[i][2]
print(ho, hol, hoi)
