#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :238
Created on Tue Aug 30 12:43:28 2022
Title: biggest of 3 nos using default arguement
@author: rahini
"""


def bot(a=10, b=20, c=30):
    big = (a if(a > c) else c) if(a > b) else (b if(b > c) else c)
    return big


# main
a = int(input('fno:'))
b = int(input('sno:'))
c = int(input('tno:'))
z1 = bot(a, b, c)
print("z1", z1)
z2 = bot(b)
print("z2", z2)
z3 = bot(c)
print("z3", z3)
z4 = bot()
print("z4", z4)
