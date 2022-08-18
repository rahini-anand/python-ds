#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :155
Created on Mon Jul 25 00:06:27 2022
Title: construct 3*3 matrix and find transpose 
@author: rahini
"""
a = []
for i in range(3):
    b = []
    for j in range(3):
        x = int(input('x='))
        b.append(x)
    a.append(b)
for i in range(3):
    for j in range(3):
        print(a[j][i])
