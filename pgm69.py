#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :69
Created on Sat Jul  9 14:55:33 2022
Title: mean of ten numbers
@author: rahini
"""
n = 0
sn = 0
cn = 0
while(n < 10):
    x = int(input('x:'))
    sn = sn+x
    cn += 1
    n += 1
mean = sn/cn
print(mean)
