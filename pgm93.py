#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :93
Created on Tue Jul 12 15:24:32 2022
Title: read a string and extract it in a reverse
@author: rahini
"""
s1 = input('Enter word:')
s2 = ''
n = len(s1)
i = 1
while(i <= n):
    s2 = s2+s1[-i]
    i += 1
print(s2)
