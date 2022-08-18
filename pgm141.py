#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :141
Created on Sun Jul 24 13:18:50 2022
Title: copy all the characters from mth position
@author: rahini
"""
s1 = input('enter word:')
s2 = ''
n = len(s1)
m = int(input('m='))
for i in range(m-1, n):
    s2 += s1[i]
print(s2)
