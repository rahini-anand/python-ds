#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :263
Created on Tue Sep 20 12:36:46 2022
Title: to construct a list using list comprehension
and swap biggest and smallest no and print in 
another fn.
@author: rahini
"""
import random
big = a[0]
small = a[0]
bp = 0
sp = 0


def swap(a):
    global big, small, bp, sp, a
    for i in range(10):
        if(a[i] > big):
            big = a[i]
            bp = i
        elif(a[i] < small):
            small = a[i]
            sp = i
        y = a[bp]
        a[bp] = a[sp]
        a[sp] = y

    def flist(a):
        for i in a:
            print(i)


# main
a = [random.randint(0, 500) for a in range(10)]
swap(a)
print(a)
