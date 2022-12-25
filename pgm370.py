#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :370
Created on Wed Dec 14 11:56:23 2022
Title: find total and average
@author: rahini
"""
import pandas as pd
import numpy as np
r = [1001, 1002, 1003, 1004, 1005]
m = np.random.randint(60, 100, (5, 5))
s = ['Tamil', 'English', 'Maths', 'Science', 'Social']
f = pd.DataFrame(m, index=r, columns=s)
f['Total'] = f['Tamil']+f['English']+f['Maths']+f['Science']+f['Social']
f['Average'] = f['Total']/5
print(f)
