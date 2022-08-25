#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :228
Created on Fri Aug 19 11:33:04 2022
Title: print header vertically
@author: rahini
"""
import csv
f = open('student biodata.csv', 'r')
x = csv.reader(f)
h = next(x)
print(h[0])
print(h[1])
print(h[2])
print(h[3])
print(h[4])
print(h[5])
print(h[6])
print(h[7])
print(h[8])
f.close()
