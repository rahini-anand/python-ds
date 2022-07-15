#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :64
Created on Sat Jul  9 14:33:03 2022
Title: read numbers other than 1000 and find sum of positive 
        negative numbers
@author: rahini
"""
x = int(input('x:'))
sp = 0
sn = 0
while(x != 1000):
    if(x > 0):
        sp = sp+x
    elif(x < 0):
        sn = sn+x
    x = int(input('x:'))
print("sum of positive numbers", sp)
print("sum of negative numbers", sn)
