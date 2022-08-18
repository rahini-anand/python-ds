#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :143
Created on Sun Jul 24 13:32:21 2022
Title: reverse the string
@author: rahini
"""
s1 = input('enter word:')
s2 = ''
n = len(s1)
for i in range(1, n+1):
    s2 += s1[-i]
print(s2)
