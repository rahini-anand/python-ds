#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :235
Created on Thu Aug 25 12:36:25 2022
Title: biggest of three nos using function
@author: rahini
"""


def bot(a, b, c):
    big = (a if(a > c) else c) if(a > b) else (b if(b > c) else c)
    return big


# main
f = int(input('fno:'))
s = int(input('sno:'))
t = int(input('tno:'))
z = bot(f, s, t)
print(z)
