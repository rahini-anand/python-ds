#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :78
Created on Sun Jul 10 19:01:30 2022
Title: to print pattern
@author: rahini
"""
i = 1
n = 1
j = 1
while(i <= 6):
    k = 1
    while(k <= n):
        print(' ', end='')
        k += 1
    m = 6
    while(j <= m):
        print('*', end='')
        m -= 1
    print()
    n += 1
    j += 1
    i += 1
