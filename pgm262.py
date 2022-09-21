#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :262
Created on Tue Sep 20 12:23:33 2022
Title: to construct a list using list comprehension
and find no of positive,negative and zero using 
global variable
@author: rahini
"""
import random
cp = 0
cn = 0
cz = 0


def count(l):
    global cp, cn, cz
    for i in l:
        if(i > 0):
            cp += 1
        elif(i < 0):
            cn += 1
        else:
            cz += 1


# main
l = [random.randint(-100, 100) for x in range(20)]
count(l)
print(l)
print(cp, cn, cz)
