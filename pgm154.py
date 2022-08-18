#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :154
Created on Mon Jul 25 00:02:58 2022
Title: construct 3*3 matrix and print element by element
@author: rahini
"""
a = []
for i in range(3):
    b = []
    for j in range(3):
        x = int(input('x='))
        b.append(x)
    a.append(b)
for k in a:
    for m in k:
        print(m)
