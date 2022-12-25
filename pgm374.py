#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :374
Created on Wed Dec 21 11:58:36 2022
Title: construct data frame from csv file
@author: rahini
"""
import pandas as pd
f = pd.read_csv('student biodata.csv')
d = pd.DataFrame(f)
print(d)
