#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :117
Created on Sat Jul 23 14:14:45 2022
Title: print nos between two limits and find it
        is odd or even
@author: rahini
"""
i = int(input('i='))
j = int(input('j='))
for x in range(i, j+1):
    if(x % 2 == 0):
        print(x, "even")
    else:
        print(x, "odd")
