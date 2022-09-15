#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :249
Created on Tue Sep  6 12:34:16 2022
Title: construct a 3*3 matrix using lambda funciton
@author: rahini
"""
import random
def m(n): return [[random.randint(0, 10)for j in range(n)]for i in range(n)]


# main
m1 = m(3)
print(m1)
