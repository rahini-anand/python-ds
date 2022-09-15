#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :259
Created on Mon Sep 12 11:57:42 2022
Title: find sum of squares of the list using
reduce and lambda function
@author: rahini
"""
from functools import reduce
import random
def l(n): return [random.randint(0, 50) for l in range(n)]


lists = l(10)
ss = reduce(lambda x, y: x+y*y, lists)
print(lists)
print(ss)
