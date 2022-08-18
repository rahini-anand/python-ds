#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :138
Created on Sun Jul 24 13:06:40 2022
Title: read a string and count no of vowels and
        constants
@author: rahini
"""
s = input('enter word:')
n = len(s)
cv = 0
cc = 0
for i in range(n):
    if(s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u'):
        cv += 1
    else:
        cc += 1
print(cv, cc)
