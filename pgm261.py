#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :261
Created on Mon Sep 12 12:34:15 2022
Title: find no of vowels and constants in a
string using global varialbe
@author: rahini
"""
cv = 0
cc = 0


def count(s):
    global cv, cc
    n = len(s)
    for i in range(n):
        if(s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u'):
            cv += 1
        else:
            cc += 1


# main
s = input('Enter word:')
count(s)
print(s)
print(cv, cc)
