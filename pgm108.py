#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :108
Created on Fri Jul 22 14:49:42 2022
Title: biggest element of each row in matrix
@author: rahini
"""
a = []
i = 0
while(i < 3):
    b = []
    j = 0
    while(j < 3):
        x = int(input('x='))
        b.append(x)
        j += 1
    a.append(b)
    i += 1
i = 0
while(i < 3):
    j = 0
    big = a[i][0]
    while(j < 3):
        if(a[i][j] > big):
            big = a[i][j]
        j += 1
    print(big)
    i += 1
