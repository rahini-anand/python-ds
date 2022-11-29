#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :338
Created on Fri Nov 18 11:57:24 2022
Title: store n students biodata into the zero array
@author: rahini
"""
import numpy as np
d = [('name', (np.str_, 10)), ('age', np.int32), ('weight', np.float32)]
a = np.zeros(10, dtype=d)
for i in range(10):
    name = input('name:')
    age = int(input('age:'))
    weight = float(input('weight:'))
    x = (name, age, weight)
    a[i] = np.array(x, d)
print(a)
f = open('npbiodata.dat', 'wb')
a.tofile("f")
f.close()
