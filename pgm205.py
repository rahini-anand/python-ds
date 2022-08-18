#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :205
Created on Tue Aug  2 11:43:16 2022
Title: construct a list that contains line no,
no. of words and no of characters
@author: rahini
"""
f = open('test.txt', 'r')
l = 1
a = []
for i in f:
    w = i.split()
    cw = len(w)
    nc = len(i)
    b = [l, cw, nc, i]
    a.append(b)
    l += 1
print(a)
f.close()
z
