#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :104
Created on Mon Jul 18 16:14:45 2022
Title: construct a list of 3*3 matrix and print 
        it element by element
@author: rahini
"""
a = []
i = 0
while(i < 3):
    b = []
    j = 0
    while(j < 3):
        x = int(input('x='))
        b.append(x)
        j += 1
    a.append(b)
    i += 1
i = 0
while(i < 3):
    j = 0
    while(j < 3):
        print(a[i][j])
        j += 1
    i += 1
