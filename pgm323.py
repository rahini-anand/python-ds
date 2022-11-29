#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :323
Created on Sat Nov  5 11:48:46 2022
Title: to construct 5*5 matrix and write it to file
@author: rahini
"""
import numpy as np
f = open('matrix.dat', 'wb')
a = np.random.randint(0, 20, (5, 5))
a.tofile("f")
f.close()
