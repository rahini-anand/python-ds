#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :360
Created on Thu Dec  8 12:10:05 2022
Title: construct 20 students 5 subject marks data frame
@author: rahini
"""
import numpy as np
import pandas as pd
r = [i for i in range(1001, 1021)]
m = np.random.randint(10, 100, (20, 5))
f = pd.DataFrame(m, index=r)
print(f)
