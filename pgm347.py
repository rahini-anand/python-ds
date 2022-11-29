#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :347
Created on Fri Nov 25 12:24:23 2022
Title: construct series of student's marks and
roll no. and perform slicing
@author: rahini
"""
import pandas as pd
import random
r = [i for i in range(1001, 1021)]
m = [random.randint(10, 100) for i in range(20)]
p = pd.Series(m, index=r)

# 1 first 10 students marks
f = p[:10]
print(f)

# 2 middle 10 students marks
mi = p[5:15]
print(mi)

# 3 last 10 students marks
l = p[10:]
print(l)

# 4 reverse the series
r = p[::-1]
print(r)
