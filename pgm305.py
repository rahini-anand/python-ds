#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :305
Created on Wed Oct 19 12:38:51 2022
Title: read data from file randomno
@author: rahini
"""
import numpy as np

f = open('randomno.dat', 'rb')
a = np.fromfile("f", dtype=np.int64)
print(a)
