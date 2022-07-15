#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :77
Created on Sun Jul 10 18:52:51 2022
Title: print pattern <|
@author: rahini
"""
i = 1
n = 5
while(i <= 6):
    k = 1
    while(k <= n):
        print(' ', end='')
        k += 1
    j = 1
    while(j <= i):
        print('*', end='')
        j += 1
    print()
    n -= 1
    i += 1
