#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :146
Created on Sun Jul 24 13:42:29 2022
Title: construct a list of n int nos and print
        it element by element
@author: rahini
"""
n = int(input('n='))
a = []
for i in range(n):
    x = int(input('x='))
    a.append(x)
for i in range(n):
    print(a[i])
