#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :73
Created on Sun Jul 10 15:59:07 2022
Title: print pattern L triangle
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
