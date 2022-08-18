#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :179
Created on Mon Jul 25 15:27:13 2022
Title: construct a tuple of n elements and 
display it and reverse it
@author: rahini
"""
import random
n = int(input('n='))
li = [random.randint(0, 1000) for x in range(n)]
a = (li)
for i in range(n):  # forward
    print(a[i])
for i in range(1, n+1):  # reverse
    print(a[-i])
