#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :340
Created on Mon Nov 21 11:36:16 2022
Title: construct a series of n random nos
@author: rahini
"""
import numpy as np
import pandas as pd
a = np.random.randint(0, 50, 10)
ps = pd.Series(a)
print(a)
print(ps)
