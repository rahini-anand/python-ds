#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :258
Created on Mon Sep 12 11:32:58 2022
Title: find sum of elements of the list using 
reduce and lambda function
@author: rahini
"""
from functools import reduce
import random
def l(n): return [random.randint(0, 50) for l in range(n)]


lists = l(10)
sums = reduce(lambda x, y: x+y, lists)
print(lists)
print(sums)
