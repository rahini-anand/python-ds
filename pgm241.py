#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :241
Created on Thu Sep  1 11:27:08 2022
Title: find biggest of 3 nos using keyword 
arguement
@author: rahini
"""


def bot(a=10, b=20, c=30):
    big = (a if(a > c) else c) if(a > b) else (b if(b > c) else c)
    return big


# main
z1 = bot(b=11, a=12, c=13)
print("z1", z1)
z2 = bot(c=15, b=14)
print("z2", z2)
z3 = bot(c=9)
print("z3", z3)
z4 = bot()
print("z4", z4)
