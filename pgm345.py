#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :345
Created on Fri Nov 25 11:47:43 2022
Title: perform slicing with index
@author: rahini
"""
import pandas as pd
m = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
     'August', 'September', 'October', 'November', 'December']
d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
p = pd.Series(d, index=m)

# 1 first 4 months
f = p[0:4]
print(f)

# 2 middle 4 months
mi = p[4:8]
print(mi)

# 3 last 4 months
l = p[8:12]
print(l)

# 4 reverse the series
r = p[::-1]
print(r)
