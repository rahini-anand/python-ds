#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :342
Created on Mon Nov 21 12:09:08 2022
Title: construct series of n random nos and 
print it in forward and backward
@author: rahini
"""
import numpy as np
import pandas as pd
a = np.random.randint(0, 50, 10)
p = pd.Series(a)
# forward direction
for i in p:
    print(i)

print()

# backward direction
for i in range(1, 11):
    print(p.values[-i])
