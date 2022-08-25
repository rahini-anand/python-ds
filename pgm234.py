#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :234
Created on Thu Aug 25 12:34:16 2022
Title: find area of circle
@author: rahini
"""


def area(r):
    a = 3.14*r*r
    return a


# main
r = int(input('radius:'))
z = area(r)
print(z)
