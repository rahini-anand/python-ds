#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :144
Created on Sun Jul 24 13:35:49 2022
Title: find given string is palindrome or not
@author: rahini
"""
s1 = input('enter word;')
s2 = ''
n = len(s1)
for i in range(1, n+1):
    s2 += s1[-i]
if(s1 == s2):
    print('Palindrome')
else:
    print("not a palindrome")
