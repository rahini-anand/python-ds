#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :133
Created on Sat Jul 23 15:02:37 2022
Title: pattern inverted pascal triangle
@author: rahini
"""
k = 0
j = 9
for i in range(5):
    print(' '*k+'*'*j)
    k += 1
    j -= 2
