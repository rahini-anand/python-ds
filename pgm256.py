#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :256
Created on Wed Sep  7 12:20:42 2022
Title: construct a list of n employee's over time
and calculate the ot amount for each employee
@author: rahini
"""
import random
def x(n): return [random.randint(0, 30) for x in range(n)]


lists = x(50)
ot = map(lambda x: x*100, lists)
ota = list(ot)
print(lists)
print(ota)
