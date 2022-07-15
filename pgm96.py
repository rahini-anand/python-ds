#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :96
Created on Thu Jul 14 13:22:30 2022
Title: contruct a list of ten integer numbers
        and print it
@author: rahini
"""
a = []
i = 0
while(i < 10):
    x = int(input('x='))
    a.append(x)
    i += 1
i = 0
while(i < 10):
    print(a[i])
    i += 1
