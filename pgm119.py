#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :119
Created on Sat Jul 23 14:21:24 2022
Title: to find the biggest and smallest of 10nos
@author: rahini
"""
big = 0
small = 1000
for i in range(10):
    x = int(input('x='))
    big = x if(x > big) else big
    small = x if(x < small) else small
print(small, big)
