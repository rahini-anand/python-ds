#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :341
Created on Mon Nov 21 11:58:07 2022
Title: construct series of n random nos and print
index,values and series
@author: rahini
"""
import numpy as np
import pandas as pd
a = np.random.randint(0, 50, 10)
p = pd.Series(a)
# indes
print(p.index)
# values
print(p.values)
# series
print(p)
