#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :67
Created on Sat Jul  9 14:43:49 2022
Title: read character other than $ and count number of upper,
        lower, digit and special character
@author: rahini
"""
ch = input('ch:')
cu = 0
cl = 0
cd = 0
cs = 0
while(ch != '$'):
    x = ord(ch)
    if(x >= 65 and x <= 90):
        cu += 1
    elif(x >= 97 and x <= 122):
        cl += 1
    elif(x >= 48 and x <= 57):
        cd += 1
    else:
        cs += 1
    ch = input('ch:')
print(cu, cl, cd, cs)
