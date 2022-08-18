#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :149
Created on Sun Jul 24 13:53:40 2022
Title: construct a list of n random nos and
        find biggest and smallest no of list
@author: rahini
"""
n = int(input('n='))
a = []
for i in range(n):
    import random
    x = random.randint(0, 1000)
    a.append(x)
print(a)
big = a[0]
small = a[0]
for i in a:
    big = i if(i > big) else big
    small = i if(i < small) else small
print(small, big)
