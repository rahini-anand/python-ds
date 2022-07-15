#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :75
Created on Sun Jul 10 18:41:19 2022
Title: print pattern inverted L triangle
@author: rahini
"""
i = 1
n = 11
while(i <= 6):
    j = 1
    while(j <= n):
        print('*', end='')
        j += 1
    print()
    n -= 2
    i += 1
