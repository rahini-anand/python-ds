#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :63
Created on Sat Jul  9 14:14:52 2022
Title: read number other than 1000 and count no. of positive,
        negative and zero
@author: rahini
"""
x = int(input('x:'))
cp = 0
cn = 0
cz = 0
while(x != 1000):
    if(x > 0):
        cp += 1
    elif(x < 0):
        cn += 1
    else:
        cz += 1
    x = int(input('x:'))
print(cp, cn, cz)
