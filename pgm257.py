#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :257
Created on Wed Sep  7 12:23:27 2022
Title: construct a list containing n students 
marks out of 75 and convert it to percentage
@author: rahini
"""
import random
def x(n): return [random.randint(0, 75) for x in range(n)]


lists = x(30)
perc = map(lambda x: x/75*100, lists)
marks = list(perc)
print(lists)
print(marks)
