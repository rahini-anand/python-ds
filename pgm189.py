#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :189
Created on Thu Jul 28 20:52:21 2022
Title: remove a particular value from set using
remove and discard method
@author: rahini
"""
n = int(input('n='))
a = set()
for i in range(n):
    import random
    x = random.randint(0, 100)
    a.add(x)
print(a)
values1 = int(input('value1='))
a.remove(values1)  # remove method
values2 = int(input('value2'))
a.discard(values2)  # discard method
print(a)
