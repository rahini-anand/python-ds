#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :153
Created on Sun Jul 24 23:59:23 2022
Title: construct 3*3 matrix and print it row by row
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
    print(k)
