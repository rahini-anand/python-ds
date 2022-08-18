#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :176
Created on Mon Jul 25 15:12:53 2022
Title: remove elements from list using pop,del
and remove
@author: rahini
"""
import random
n = int(input('n='))
a = [random.randint(0, 1000) for i in range(n)]
print(a)
x = int(input('x='))
a.remove(x)  # remove value x from a
print(a)
a.pop(5)  # remove values in index 5 of a
print(a)
del(a[7])  # remove value in index 7 of a
print(a)
del(a)  # remove list a
