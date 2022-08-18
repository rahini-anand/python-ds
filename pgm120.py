#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :120
Created on Sat Jul 23 14:26:44 2022
Title: to generate n random int no and print it
@author: rahini
"""
n = int(input('n='))
for i in range(n):
    import random
    x = random.randint(-1000, 1000)
    print(x)
