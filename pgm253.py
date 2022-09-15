#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :253
Created on Tue Sep  6 13:10:42 2022
Title: extract single digit numbers from list 
using lambda function
@author: rahini
"""
import random
def x(n): return [random.randint(0, 25) for x in range(n)]


lists = x(15)

ex = filter(lambda x: x >= 0 and x <= 9, lists)
# main
print(lists)
sd = list(ex)
print(sd)
