#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :91
Created on Tue Jul 12 15:18:19 2022
Title: copy n characters from mth position
@author: rahini
"""
s1 = input('Enter word:')
s2 = ''
n = int(input('n='))
m = int(input('m='))
i = m-1
while(i < m+n-1):
    s2 = s2+s1[i]
    i += 1
print(s2)
