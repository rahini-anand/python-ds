#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :329
Created on Wed Nov  9 12:06:07 2022
Title: construct a boolean array from numpy array
of n random nos
@author: rahini
"""
import numpy as np
import random
l = [random.randint(80, 160, (50)) for x in range(50)]
a = np.array(l)
print(a)
b = a > 100
print(b)
