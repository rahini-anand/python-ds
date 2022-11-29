#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :348
Created on Sat Nov 26 11:51:03 2022
Title: construct series of marks and roll no and 
perform scalar addition
@author: rahini
"""
import pandas as pd
import random

r = [i for i in range(1001, 1021)]
m1 = [random.randint(10, 100) for i in range(20)]
m2 = [random.randint(10, 100) for i in range(20)]
p1 = pd.Series(m1, index=r)
p2 = pd.Series(m2, index=r)
print(p1)
print(p2)
