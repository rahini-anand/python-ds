#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :25
Created on Sun Jun 26 14:23:35 2022
Title: given year leap year or not
@author: rahini
"""
x = int(input('year:'))
if(x % 4 == 0):
    print("leap year")
else:
    print("not a leap year")
