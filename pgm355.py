#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :355
Created on Mon Dec  5 12:19:48 2022
Title: 
@author: rahini
"""
import pandas as pd
import random
n = [random.randint(10, 50) for i in range(20)]
s = pd.Series(n)
print(s)

# unique elements in series
u = s.unique()
print("unique elements", u)

# no of unique elements
u1 = s.nunique()
print("no of unique elements", u1)

# frequency count of elements
f = s.value_counts()
print("frequency", f)

# discrete
d = s.describe()
print("describe", d)
