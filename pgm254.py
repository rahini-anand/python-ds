#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :254
Created on Wed Sep  7 11:29:29 2022
Title: construct a list of positive and negative
nos and extract positive and negative nos
@author: rahini
"""
import random
def x(n): return [random.randint(-100, 100) for x in range(n)]


lists = x(30)
p = filter(lambda x: x >= 0, lists)
n = filter(lambda x: x < 0, lists)
# main
print(lists)
pex = list(p)
nex = list(n)
print(pex)
print(nex)
