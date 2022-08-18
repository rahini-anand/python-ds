#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :170
Created on Mon Jul 25 14:42:48 2022
Title: construct a list of n students mark from
0 to 100 and convert marks which is 35 to 39
into 40 using list comprehension
@author: rahini
"""
import random
n = int(input('n='))
a = [random.randint(0, 100) for x in range(n)]
print(a)
c = [40 if(i >= 35 and i <= 39) else i for i in a]
print(c)
