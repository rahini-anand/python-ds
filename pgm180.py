#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :180
Created on Mon Jul 25 15:33:55 2022
Title: construct a tuple of n elements and find
biggest and smallest element of tuple
@author: rahini
"""
import random
n = int(input('n='))
li = [random.randint(0, 1000) for x in range(n)]
a = (li)
print(a)
big = a[0]
small = a[0]
for i in range(n):
    big = a[i] if (a[i] > big) else big
    small = a[i] if (a[i] < small) else small
print(small, big)
