#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :98
Created on Thu Jul 14 13:31:07 2022
Title: to construct a list of 10 int nos and 
    find the biggest and smallest element of the list
@author: rahini
"""
a = []
i = 0
while(i < 10):
    print(i+1, '=', end='')
    x = int(input())
    a.append(x)
    i += 1
    print()
i = 0
big = a[0]
small = a[0]
while(i < 10):
    big = a[i] if a[i] > big else big
    small = a[i] if a[i] < small else small
    i += 1
print(big, small)
