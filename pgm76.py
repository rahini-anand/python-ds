#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :76
Created on Sun Jul 10 18:43:32 2022
Title: print pattern |>
@author: rahini
"""
i = 1
while(i <= 6):
    j = 1
    while(j <= i):
        print('*', end='')
        j += 1
    print()
    i += 1
i = 1
n = 5
while(i <= 5):
    j = 1
    while(j <= n):
        print('*', end='')
        j += 1
    print()
    n -= 1
    i += 1
