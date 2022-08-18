#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :202
Created on Mon Aug  1 11:47:32 2022
Title: display a text file line by line
@author: rahini
"""
f = open('test.txt', 'r')
for i in f:
    print(i, end='')
f.close()
