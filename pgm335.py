#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :335
Created on Wed Nov 16 12:00:57 2022
Title: construct heterogeneous array and display it
@author: rahini
"""
import numpy as np
d = [('name', (np.str_, 10)), ('age', np.int32), ('weight', np.float32)]
l = ("Rahini", 29, 57.7)
a = np.array(l, d)
print(a)
