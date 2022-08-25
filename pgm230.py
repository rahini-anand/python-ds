#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :230
Created on Fri Aug 19 11:52:05 2022
Title: print row in vertical column
@author: rahini
"""
import csv
f = open('student biodata.csv', 'r')
x = csv.reader(f)
h = next(x)
for i in x:
    print(h[0], i[0])
    print(h[1], i[1])
    print(h[2], i[2])
    print(h[3], i[3])
    print(h[4], i[4])
    print(h[5], i[5])
    print(h[6], i[6])
    print(h[7], i[7])
    print(h[8], i[8])
f.close()
