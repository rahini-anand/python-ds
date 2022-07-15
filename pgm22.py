#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :22
Created on Sun Jun 26 14:11:25 2022
Title: find biggest of three numbers
@author: rahini
"""
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if(a > b):
    if(a > c):
        print("greater number is", a)
    else:
        print("greater number is", c)
else:
    if(b > c):
        print("greater number is", b)
    else:
        print("greater number is", c)
