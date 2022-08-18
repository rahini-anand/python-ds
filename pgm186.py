#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :186
Created on Thu Jul 28 20:39:03 2022
Title: construct two sets of int nos and make it
one using update method
@author: rahini
"""
import random
n = int(input('n='))
a = [random.randint(0, 100) for x in range(n)]
b = [random.randint(0, 100) for y in range(n)]
print(a)
print(b)
s1 = set(a)
s2 = set(b)
s1 = s1.update(s2)
print(s1)
