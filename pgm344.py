#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :344
Created on Tue Nov 22 12:21:27 2022
Title: construct a pandas series of month and its days
@author: rahini
"""
import pandas as pd
m = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
     'August', 'September', 'October', 'November', 'December']
d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
p = pd.Series(d, index=m)
print(p)
