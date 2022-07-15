#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :80
Created on Sun Jul 10 19:44:27 2022
Title:print pascal triangle ^
@author: rahini
"""
i = 1
j = 1
n = 5
while(i <= 6):
    k = 1
    while(k <= n):
        print(' ', end='')
        k += 1
    m = 1
    while(m <= j):
        print('*', end='')
        m += 1
    print()
    j += 2
    n -= 1
    i += 1
