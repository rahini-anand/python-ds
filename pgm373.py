#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :373
Created on Wed Dec 21 11:46:05 2022
Title: construct data frame using dictionary
@author: rahini
"""
import pandas as pd
d = {}
for i in range(5):
    name = input('name:')
    age = int(input('age:'))
    gender = input('gender:')
    d[name] = [age, gender]
f = pd.DataFrame(d)
print(f)
