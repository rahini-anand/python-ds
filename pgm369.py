#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :369
Created on Wed Dec 14 11:41:56 2022
Title: insert total column
@author: rahini
"""
import pandas as pd
import numpy as np
r = [1001, 1002, 1003, 1004, 1005]
m = np.random.randint(60, 100, (5, 5))
s = ['Tamil', 'English', 'Maths', 'Science', 'Social']
f = pd.DataFrame(m, index=r, columns=s)
f['Total'] = f['Tamil']+f['English']
print(f)
