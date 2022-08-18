#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :183
Created on Thu Jul 28 20:33:59 2022
Title: construct a set of n int nos and print it
@author: rahini
"""
a = set()
n = int(input('n='))
for i in range(n):
    x = int(input('x='))
    a.add(x)
print(a)
