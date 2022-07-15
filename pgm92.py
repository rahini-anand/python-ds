#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :92
Created on Tue Jul 12 15:21:00 2022
Title: extract last n characters
@author: rahini
"""
s1 = input('Enter word')
s2 = ''
length = len(s1)
n = int(input('n='))
m = length-n
i = m
while(i < length):
    s2 = s2+s1[i]
    i += 1
print(s2)
