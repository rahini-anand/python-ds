#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :237
Created on Tue Aug 30 12:33:28 2022
Title: find sum of two int nos using default
arguement
@author: rahini
"""


def sum(a=10, b=20):
    c = a+b
    return c


# main
a = int(input('a='))
b = int(input('b='))
c1 = sum(a, b)
print("c1", c1)
c2 = sum(b)
print("c2", c2)
c3 = sum()
print("c3", c3)
