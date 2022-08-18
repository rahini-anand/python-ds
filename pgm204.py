#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :204
Created on Mon Aug  1 12:12:53 2022
Title: print no. of upper,lower,digit and special
character in each line
@author: rahini
"""
f = open('test.txt', 'r')
l = 1
for i in f:
    cu = 0
    cl = 0
    cd = 0
    cs = 0
    for j in i:
        x = ord(j)
        if(x >= 65 and x <= 90):
            cu += 1
        elif(x >= 97 and x <= 122):
            cl += 1
        elif(x >= 48 and x <= 57):
            cd += 1
        else:
            cs += 1
    print(l, cu, cl, cd, cs)
    l += 1
f.close()
