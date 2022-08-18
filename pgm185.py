#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :185
Created on Thu Jul 28 20:36:15 2022
Title: construct a list using list comprehension
and construct a set from list
@author: rahini
"""
import random
n = int(input('n='))
a = [random.randint(0, 100) for x in range(n)]
s = set(a)
print(s)
