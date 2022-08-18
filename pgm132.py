#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :132
Created on Sat Jul 23 15:02:37 2022
Title: pattern
@author: rahini
"""
k = 5
for i in range(1, 7):
    print(' '*k+'*'*i)
    k -= 1
k = 1
j = 5
for i in range(6):
    print(' '*k+'*'*j)
    k += 1
    j -= 1
