#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :356
Created on Tue Dec  6 11:50:31 2022
Title: to perform sorting function
@author: rahini
"""
import pandas as pd
import random
r1 = [i for i in range(1001, 1021)]
m1 = [random.randint(10, 100) for i in range(20)]
s = pd.Series(m1, index=r1)
print(s)

# ascending values
a1 = s.sort_values()
print(a1)

# descending values
d1 = s.sort_values(ascending=False)
print(d1)

# ascending index
a2 = s.sort_index()
print(a2)

# descending index
d2 = s.sort_index(ascending=False)
print(d2)
