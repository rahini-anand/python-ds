#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :359
Created on Thu Dec  8 11:55:50 2022
Title: construt data frame and print it
@author: rahini
"""
import numpy as np
import pandas as pd
x = np.random.randint(0, 20, (5, 5))
f = pd.DataFrame(x)
print(f)
