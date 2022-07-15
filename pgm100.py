#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :100
Created on Thu Jul 14 13:59:40 2022
Title: find the biggest and second biggest of 
    ten no int list
@author: rahini
"""
a = []
i = 0
while(i < 10):
    x = int(input('x:'))
    a.append(x)
    i += 1
i = 0
big = a[0]
while(i < 10):
    big = a[i] if a[i] > big else big
    i += 1
i = 0
sbig = a[0]
while(i < 10):
    if(a[i] > sbig and a[i] != big):
        sbig = a[i]
    i += 1
print(big, sbig)
