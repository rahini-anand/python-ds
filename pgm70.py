#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :70
Created on Sat Jul  9 14:58:53 2022
Title: biggest and smallest of ten numbers
@author: rahini
"""
n = 0
big = 0
small = 1000
while(n < 10):
    x = int(input('x:'))
    if(x > big):
        big = x
    if(x < small):
        small = x
    n += 1
print(small, big)
