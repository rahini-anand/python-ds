#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :167
Created on Mon Jul 25 14:32:33 2022
Title: construct a list of n random nos using
list comprehension
@author: rahini
"""
import random
n = int(input('n='))
a = [random.randint(0, 100) for x in range(n)]
print(a)
