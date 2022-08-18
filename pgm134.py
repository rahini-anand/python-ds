#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :134
Created on Sun Jul 24 12:49:07 2022
Title: print diamond pattern
@author: rahini
"""
k = 4
j = 1
for i in range(5):
    print(' '*k+'*'*j)
    k -= 1
    j += 2
k = 1
j = 7
for i in range(4):
    print(' '*k+'*'*j)
    k += 1
    j -= 2
