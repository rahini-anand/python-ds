#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :358
Created on Tue Dec  6 12:15:18 2022
Title: construct series using dictionary
@author: rahini
"""
import pandas as pd
d = {}
for i in range(12):
    month = input('month:')
    days = int(input('days:'))
    d[month] = days
print(d)

s = pd.Series(d)
print(s)
