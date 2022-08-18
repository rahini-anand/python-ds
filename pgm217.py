#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :217
Created on Fri Aug 12 11:41:02 2022
Title: to count the positive,negative and zero
in the file
@author: rahini
"""
import pickle
f = open('list.dat', 'rb')
x = pickle.load(f)
cp = 0
cn = 0
cz = 0
print(x)
for i in x:
    if(i > 0):
        cp += 1
    elif(i < 0):
        cn += 1
    else:
        cz += 1
print(cp, cn, cz)
