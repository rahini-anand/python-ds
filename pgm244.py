#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :244
Created on Thu Sep  1 12:15:51 2022
Title: find the sum of args that are passed to 
the functions
@author: rahini
"""


def f1(*a):
    sums = 0
    for i in a:
        sums = i+sums
    return sums


# main
s1 = f1(1, 2, 3)
print(s1)
s2 = f1(4, 5, 6)
print(s2)
s3 = f1(7, 8, 9, 10)
print(s3)
