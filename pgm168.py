#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :168
Created on Mon Jul 25 14:36:22 2022
Title: construct the list of n  nos and
extract only the list of even nosrandom
@author: rahini
"""
import random
n = int(input('n='))
a = [random.randint(0, 1000) for x in range(n)]
print(a)
even = [i for i in a if(i % 2 == 0)]
print(even)
