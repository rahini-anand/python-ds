#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :177
Created on Mon Jul 25 15:22:16 2022
Title: reverse the list,assending and desending
@author: rahini
"""
import random
n = int(input('x='))
a = [random.randint(0, 1000) for x in range(n)]
print(a)
a.reverse()
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
