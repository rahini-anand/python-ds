#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :140
Created on Sun Jul 24 13:15:38 2022
Title: to copy left n characters of the string
@author: rahini
"""
s1 = input('Enter word:')
s2 = ''
n = int(input('n='))
for i in range(n):
    s2 += s1[i]
print(s2)
