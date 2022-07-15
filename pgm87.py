#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :87o
Created on Tue Jul 12 14:49:55 2022
Title: Read a string and concatenate or copy it
        to another string
@author: rahini
"""
s1 = input('Enter word:')
s2 = []
n = len(s1)
i = 0
while(i < n):
    s2 = s2+s1[i]
    i += 1
print(s2)
