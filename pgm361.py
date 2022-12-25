#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :361
Created on Thu Dec  8 12:17:17 2022
Title: construt data frame using column indexing
@author: rahini
"""
import numpy as np
import pandas as pd
r = [i for i in range(1001, 1021)]
m = np.random.randint(10, 100, (20, 5))
s = ['Tamil', 'English', 'Maths', 'Science', 'Social']
f = pd.DataFrame(m, index=r, columns=s)
print(f)
