#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :332
Created on Thu Nov 10 11:53:45 2022
Title: to find out transpose,diagonal and trace 
of the matrix
@author: rahini
"""
import numpy as np
a = np.random.randint(0, 5, (5, 5))
x = a.reshape(5, 5)
print(x)
# 1.transpose
t = x.transpose()
print(t)

# 2 diagonal
d = x.diagonal()
print(d)

# 3 trace
tc = x.trace()
print(tc)
