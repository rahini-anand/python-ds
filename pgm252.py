#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :252
Created on Tue Sep  6 13:01:58 2022
Title: extrct even numbers from list using 
lambda funciton
@author: rahini
"""
import random
def x(n): return [random.randint(0, 100) for x in range(n)]


lists = x(20)
ex = filter(lambda y: y % 2 == 0, lists)
# main

print(lists)
y = list(ex)
print(y)
