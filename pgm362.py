#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :362
Created on Fri Dec  9 11:51:59 2022
Title: construct 20 students marks and print each subject
@author: rahini
"""
import numpy as np
import pandas as pd
r = [i for i in range(1001, 1021)]
m = np.random.randint(10, 100, (20, 5))
s = ['Tamil', 'English', 'Maths', 'Science', 'Social']
f = pd.DataFrame(m, index=r, columns=s)
print(f['Tamil'])
print(f['English'])
print(f['Maths'])
print(f['Science'])
print(f['Social'])
