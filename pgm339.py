#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :339
Created on Fri Nov 18 12:07:54 2022
Title: to read biodata from file and display it
@author: rahini
"""
import numpy as np
f = open('npbiodata.dat', 'rb')
d = [('name', (np.str_, 10)), ('age', np.int32), ('weight', np.float32)]
x = np.fromfile("f", dtype=d)
print(x)
