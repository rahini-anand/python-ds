#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :239
Created on Thu Sep  1 11:19:16 2022
Title: find biggest and smallest of 3 nos
using default arguement
@author: rahini
"""


def bns(a=1, b=5, c=10):
    big = (a if(a > c) else c) if(a > b) else (b if(b > c) else c)
    small = (a if(a < c) else c) if(a < b) else (b if(b < c) else c)
    return big, small


# main
a = int(input('fno:'))
b = int(input('sno:'))
c = int(input('tno:'))
z1 = bns(a, b, c)
print(z1)
z2 = bns(b, c)
print(z2)
z3 = bns(c)
print(z3)
z4 = bns()
print(z4)
