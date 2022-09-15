#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :245
Created on Thu Sep  1 12:18:23 2022
Title: find biggest and smallest element of 
argument in funciton
@author: rahini
"""


def f1(*a):
    big = 0
    small = 100
    for i in a:
        big = i if(i > big) else big
        small = i if(i < small) else small
    return small, big


# main
v1 = f1(1, 2, 3, 10, 6, 35, 99)
print(v1)
v2 = f1(10, 20, 5, 3, 7, 49)
print(v2)
