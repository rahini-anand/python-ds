#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :192
Created on Thu Jul 28 21:05:38 2022
Title: to count the frequency of nos in the list
@author: rahini
"""
import random
n = int(input('n='))
a = [random.randint(0, 100) for x in range(n)]
s = set(a)
print(a)
print(s)
for i in s:
    counts = a.count(i)
    print(i, counts)
