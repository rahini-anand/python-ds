#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :65
Created on Sat Jul  9 14:37:01 2022
Title: read numbers other than 1000 and find average of 
        positive and negative numbers
@author: rahini
"""
x = int(input('x:'))
cp = 0
cn = 0
sp = 0
sn = 0
while(x != 1000):
    if(x > 0):
        cp += 1
        sp = sp+x
    elif(x < 0):
        cn += 1
        sn = sn+x
    x = int(input('x:'))
ap = sp/cp
an = sn/cn
print("Average of positive numbers", ap)
print("average of negative numbers", an)
