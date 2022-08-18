#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :203
Created on Mon Aug  1 12:00:21 2022
Title: display a file with line number
@author: rahini
"""
f = open('test.txt', 'r')
l = 1
for i in f:
    print(l, i, end='')
    l += 1
f.close()
