#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :236
Created on Thu Aug 25 12:40:35 2022
Title: biggest and smallest of three nos
@author: rahini
"""


def bns(a, b, c):
    big = (a if(a > c) else c) if(a > b) else (b if(b > c) else c)
    small = (a if(a < c) else c) if(a < b) else (b if(b < c) else c)
    return big, small


# main
f = int(input('fno:'))
s = int(input('sno:'))
t = int(input('tno:'))
z = bns(f, s, t)
print(z)
