#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :372
Created on Thu Dec 15 12:15:38 2022
Title: perform head tail and describe function
@author: rahini
"""
import numpy as np
import pandas as pd
r = [i for i in range(1001, 1021)]
m = np.random.randint(10, 100, (20, 5))
s = ['Tamil', 'English', 'Maths', 'Science', 'Social']
f = pd.DataFrame(m, index=r, columns=s)

# head (first 10 elements)
f1 = f.head(10)
print(f1)

# tail (last n elements)
f2 = f.tail(10)
print(f2)

# describe
f3 = f.describe()
print(f3)
