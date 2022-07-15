#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :23
Created on Sun Jun 26 14:17:15 2022
Title: smallest of three int numbers
@author: rahini
"""
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if(a < b):
    if(a < c):
        print("smallest number is", a)
    else:
        print("smallest number is", c)
else:
    if(b < c):
        print("smallest number is", b)
    else:
        print("smallest number is", c)
