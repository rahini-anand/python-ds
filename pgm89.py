#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :89
Created on Tue Jul 12 15:09:41 2022
Title: to read string and copy first n character
        to another string
@author: rahini
"""
s1 = input('enter word:')
s2 = []
n = int(input('n:'))
i = 0
while(i < n):
    s2 = s2+s1[i]
    i += 1
print(s2)
