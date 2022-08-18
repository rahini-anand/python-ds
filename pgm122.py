#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :122
Created on Sat Jul 23 14:37:57 2022
Title: find the biggest and smallest of n random
        nos
@author: rahini
"""
n = int(input('n='))
big = 0
small = 0
for i in range(n):
    import random
    x = random.randint(-1000, 1000)
    big = x if(x > big) else big
    small = x if(x < small) else small
    print(x)
print(small, big)
