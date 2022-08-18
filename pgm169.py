#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :169
Created on Mon Jul 25 14:40:18 2022
Title: construct a list of n random nos and 
extract only nos divisible by 3,5and7
@author: rahini
"""
import random
n = int(input('n='))
a = [random.randint(0, 1000) for x in range(n)]
print(a)
ex = [i for i in a if(i % 3 == 0 and i % 5 == 0 and i % 7 == 0)]
print(ex)
