#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :336
Created on Thu Nov 17 12:03:26 2022
Title: construct heterogeneous array using dictionary
@author: rahini
"""
import numpy as np
d = {'names': ('name', 'age', 'weight'),
     'formats': ((np.str_, 10), (np.int32), (np.float32))}
x = ('Rahini', 29, 57.7)
a = np.array(x, d)
print(a)
