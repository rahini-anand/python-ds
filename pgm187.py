#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :187
Created on Thu Jul 28 20:43:54 2022
Title: construct a set of n int nos and print
elements in set
@author: rahini
"""
n = int(input('n='))
a = set()
for i in range(n):
    import random
    x = random.randint(0, 100)
    a.add(x)
for i in a:
    print(i)
