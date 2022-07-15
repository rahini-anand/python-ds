#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :85
Created on Tue Jul 12 14:40:44 2022
Title: to read a string and count number of 
        vowels and constants in it
@author: rahini
"""
s = input('Enter word:')
n = len(s)
i = 0
cv = 0
cc = 0
while(i < n):
    if(s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u'):
        cv += 1
    else:
        cc += 1
    i += 1
print(cv, cc)
