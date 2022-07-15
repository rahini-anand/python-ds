#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :94
Created on Tue Jul 12 15:27:01 2022
Title: to find given string is palindrome or not
@author: rahini
"""
s1 = input('Enter word:')
s2 = ''
n = len(s1)
i = 1
while(i <= n):
    s2 = s2+s1[-i]
    i += 1
if(s2 == s1):
    print("string is palindrome")
else:
    print("string is not a palindrome")
