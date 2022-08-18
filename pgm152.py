#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :152
Created on Sun Jul 24 23:56:41 2022
Title: construct a 3*3 matrix and print it
@author: rahini
"""
a = []
for i in range(3):
    b = []
    for j in range(3):
        x = int(input('x='))
        b.append(x)
    a.append(b)
print(a)
