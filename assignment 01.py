#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no : Assignment 01
Created on Mon Jun 27 14:34:01 2022
Title: print hollow triangle
@author: rahini
"""
i = 1
n = 6
k = 1
while(k <= n):
    print(' ', end='')
    k = k+1
print('*', end='')
print()
i = 2
n = 5
j = 1
while(i <= 6):
    k = 1
    while(k <= n):
        print(' ', end='')
        k = k+1
    print('*', end='')
    m = 1
    while(m <= j):
        print(' ', end='')
        m = m+1
    print('*', end='')
    print()
    i = i+1
    n = n-1
    j = j+2
i = 7
l = 1
while(l <= 6):
    print('*', end='')
    print(' ', end='')
    l = l+1
print('*', end='')
print()
