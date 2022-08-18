#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :171
Created on Mon Jul 25 14:47:20 2022
Title: construct a 3*3 matrix using nested loop
and list comprehension
@author: rahini
"""
import random
a = [[
    random.randint(0, 1000)
    for i in range(3)]
    for j in range(3)
]
print(a)
