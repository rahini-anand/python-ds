#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :306
Created on Fri Oct 21 12:07:41 2022
Title: to read from file and construct positive
and negative array out of it
@author: rahini
"""
import numpy as np
f = open('randomno.dat', 'rb')
a = np.fromfile("f", dtype=np.int64)
p = []
n = []
for i in a:
    if(i >= 0):
        p.append(i)
    else:
        n.append(i)
pa = np.array(p)
na = np.array(n)
print(pa)
print(na)
