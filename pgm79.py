#!/ßusr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :79
Created on Sun Jul 10 19:13:21 2022
Title: print pattern
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
i = 1
n = 1
j = 5
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
    n += 1
    j -= 1
    i += 1
