#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :243
Created on Thu Sep  1 12:13:45 2022
Title: print the values that are passed to the 
functions
@author: rahini
"""


def f1(*a):
    for i in a:
        print(i)


# main
f1(10)
f1(10, 20)
f1(10, 20, 30)
f1(10, 20, 30, 40)
f1(10, 20, 30, 40, 50)
