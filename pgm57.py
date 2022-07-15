#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :57
Created on Sat Jul  9 13:47:51 2022
Title: print numbers from 1 to 100 and find it even or odd
@author: rahini
"""
x = 1
while(x <= 100):
    if(x % 2 == 0):
        print("even number", x)
    else:
        print("odd number", x)
    x += 1
