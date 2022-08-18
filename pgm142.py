#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :142
Created on Sun Jul 24 13:25:44 2022
Title: to copy last n characters
@author: rahini
"""
s1 = input('enter word:')
s2 = ''
length = len(s1)
n = int(input('n='))
m = length-n
for i in range(m, length):
    s2 += s1[i]
print(s2)
