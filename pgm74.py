#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :74
Created on Sun Jul 10 16:04:14 2022
Title: print pattern L triangle with two increment
@author: rahini
"""
i = 1
n = 1
while(i <= 6):
    j = 1
    while(j <= n):
        print('*', end='')
        j = j+1
    print()
    n += 2
    i += 1
