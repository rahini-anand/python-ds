#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :102
Created on Mon Jul 18 16:08:09 2022
Title: construct a list of 3*3 matrix
@author: rahini
"""
a = []
i = 0
while(i < 3):
    b = []
    j = 0
    while(j < 3):
        x = int(input('X='))
        b.append(x)
        j += 1
    a.append(b)
    i += 1
print(a)
