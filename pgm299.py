#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no : 299
Created on Tue Oct 18 11:45:55 2022
Title: to construct a numpy array
@author: rahini
"""
import numpy as np
import random

l = [random.randint(0, 100) for i in range(20)]
npl = np.array(l)
print(npl)
