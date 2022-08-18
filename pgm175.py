#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :175
Created on Mon Jul 25 15:06:28 2022
Title: construct a list of n nos and display 
it in reverse using pop
@author: rahini
"""
n = int(input('n='))
a = [int(input('no:')) for i in range(n)]
print(a)
for i in range(n):
    x = a.pop()
    print(x)
print(a)
