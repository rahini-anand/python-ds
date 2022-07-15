#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :90
Created on Tue Jul 12 15:14:40 2022
Title: copy all the characters from the mth position
@author: rahini
"""
s1 = input('Enter word:')
n = len(s1)
s2 = ''
m = int(input('m:'))
i = m-1
while(i < n):
    s2 = s2+s1[i]
    i += 1
print(s2)
