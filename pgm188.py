#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :188
Created on Thu Jul 28 20:48:35 2022
Title: construct set and delete elements one by
one using pop
@author: rahini
"""
n = int(input('n='))
a = set()
for i in range(n):
    import random
    x = random.randint(0, 100)
    a.add(x)
print(a)
for i in range(n):
    y = a.pop()
    print(y)
print(a)
