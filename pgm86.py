#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :86
Created on Tue Jul 12 14:44:50 2022
Title: to read string and count number of upper,
        lower, digits and special character
@author: rahini
"""
s = input('Enter word:')
n = len(s)
i = 0
cu = 0
cl = 0
cd = 0
cs = 0
while(i < n):
    x = ord(s[i])
    if(x >= 65 and x <= 90):
        cu += 1
    elif(x >= 97 and x <= 122):
        cl += 1
    elif(x >= 48 and x <= 57):
        cd += 1
    else:
        cs += 1
    i += 1
print(cu, cl, cd, cs)
