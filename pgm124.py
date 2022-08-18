#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :124
Created on Sat Jul 23 14:43:22 2022
Title: print patter pascal triangle
@author: rahini
"""
k = 4
j = 1
for i in range(5):
    print(' '*k+'*'*j)
    k -= 1
    j += 2
