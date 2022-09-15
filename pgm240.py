#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :240
Created on Thu Sep  1 11:24:46 2022
Title: find sum of 2 nos using keyword arguement
@author: rahini
"""


def sum(a=10, b=20):
    c = a+b
    return c


# main
c1 = sum(b=11, a=21)
print(c1)
c2 = sum(b=12)
print(c2)
c3 = sum()
print(c3)
