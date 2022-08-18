#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :226
Created on Thu Aug 18 11:48:56 2022
Title: print the header of the file outside 
loop and data inside the loop
@author: rahini
"""
import csv
f = open('student biodata.csv', 'r')
x = csv.reader(f)
h = next(x)
print(h)
for i in x:
    print(i)
f.close()
