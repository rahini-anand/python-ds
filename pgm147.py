#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :147
Created on Sun Jul 24 13:45:37 2022
Title: construct list of n int nos and print
        it in reverse
@author: rahini
"""
a = []
n = int(input('n='))
for i in range(n):
    x = int(input('x='))
    a.append(x)
for i in range(1, n+1):
    print(a[-i])
