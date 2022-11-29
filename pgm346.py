#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :346
Created on Fri Nov 25 12:06:30 2022
Title: perform slicing using string index
@author: rahini
"""
import pandas as pd
m = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
     'August', 'September', 'October', 'November', 'December']
d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
p = pd.Series(d, index=m)

# 1 first 4 months
f = p[:'April']
print(f)

# 2 middle 4 months
mi = p['May':'August']
print(mi)

# 3 last 4 months
l = p['September':]
print(l)

# 4 reverse the series
r = p[::-1]
print(r)
