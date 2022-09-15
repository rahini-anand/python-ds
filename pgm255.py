#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :255
Created on Wed Sep  7 12:12:51 2022
Title: construct a list of n nos and find out
its square 
@author: rahini
"""
import random
def x(n): return [random.randint(0, 100) for x in range(n)]


lists = x(20)
s = map(lambda x: x*x, lists)
sq = list(s)
print(lists)
print(sq)
