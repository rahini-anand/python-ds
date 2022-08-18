#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :139
Created on Sun Jul 24 13:10:39 2022
Title: read a string and count no of upper,
        lower,digits and special characters
@author: rahini
"""
s = input('enter word:')
n = len(s)
cu = 0
cl = 0
cd = 0
cs = 0
for i in range(n):
    x = ord(s[i])
    if(x >= 65 and x <= 90):
        cu += 1
    elif(x >= 97 and x <= 122):
        cl += 1
    elif(x >= 48 and x <= 57):
        cd += 1
    else:
        cs += 1
print(cu, cl, cd, cs)
