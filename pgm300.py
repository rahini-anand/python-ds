#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :300
Created on Tue Oct 18 11:57:32 2022
Title: construct numpy array and print it in 
3 ways
@author: rahini
"""
import numpy as np
import random

l = [random.randint(0, 100) for i in range(20)]
npl = np.array(l)
# 1(element by element using index)
for i in range(20):
    print(npl[i])

# 2(reverse order)
for i in range(1, 21):
    print(npl[-i])
# 3(iteration)
for i in npl:
    print(i)
