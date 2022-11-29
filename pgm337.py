#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :337
Created on Thu Nov 17 12:18:10 2022
Title: read biodata from kb and display it as 
heterogeneous array
@author: rahini
"""
import numpy as np
d = [('name', (np.str_, 10)), ('age', np.int32), ('weight', np.float32)]
name = input('name:')
age = int(input('age:'))
weight = float(input('weight:'))
l = (name, age, weight)
a = np.array(l, d)
print(a)
