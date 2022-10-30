#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :304
Created on Wed Oct 19 12:20:35 2022
Title: generate n random nos and write it 
in a file
@author: rahini
"""
import numpy as np

f = open('randomno.dat', 'wb')
n = int(input('n='))
a = np.random.randint(-1000, 1000, n)
a.tofile("f")
print(a)
