#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :88
Created on Tue Jul 12 14:56:12 2022
Title: to read a string a convert upper to lower
        case and copy it to another string
@author: rahini
"""
s1 = input('Enter word:')
s2 = ''
n = len(s1)
i = 0
while(i < n):
    x = ord(s1[i])
    if(x >= 65 and x <= 90):
        s2 = s2+(chr(x+32))
    elif(x >= 97 and x <= 122):
        s2 = s2+(chr(x-32))
    else:
        s2 = s2+s1[i]
    i += 1
print(s2)
