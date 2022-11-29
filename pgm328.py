#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :328
Created on Wed Nov  9 11:43:31 2022
Title: 
@author: rahini
"""
import numpy as np
import random
l = [random.randint(0, 6) for x in range(25)]
print(l)
a = np.array(l, dtype=bool)
print(a)
