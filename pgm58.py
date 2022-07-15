#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :58
Created on Sat Jul  9 13:50:22 2022
Title: print years from 1000 to 2000 and find it leap year or not
@author: rahini
"""
x = 1000
while(x <= 2000):
    if(x % 4 == 0):
        print(x, "leap year")
    else:
        print(x, "not a leap year")
    x += 1
