#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :81
Created on Sun Jul 10 19:50:46 2022
Title: print inverted pascal triangle
@author: rahini
"""
i = 1
j = 9
n = 0
while(i <= 5):
    k = 1
    while(k <= n):
        print(' ', end='')
        k += 1
    m = 1
    while(m <= j):
        print('*', end='')
        m += 1
    print()
    i += 1
    n += 1
    j -= 2
