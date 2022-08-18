#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :215
Created on Tue Aug  9 12:20:45 2022
Title: to generate a list of n random nos and
dump it in one file
@author: rahini
"""
import random
import pickle
n = int(input('n='))
x = [random.randint(0, 1000) for x in range(n)]
f = open('list.dat', 'wb')
pickle.dump(x, f)
f.close()
