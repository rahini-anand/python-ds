#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :343
Created on Tue Nov 22 12:05:33 2022
Title: construct a pandas series of 20 students 
marks and roll no as index
@author: rahini
"""
import random
import pandas as pd
m = [random.randint(0, 100) for i in range(20)]
r = [int(input('rno:')) for i in range(20)]
p = pd.Series(m, index=r)
print(p)
