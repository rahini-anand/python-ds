#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :260
Created on Mon Sep 12 12:46:26 2022
Title: find  no of vowels and constants in a 
string
@author: rahini
"""


def counts(s):
    n = len(s)
    cv = 0
    cc = 0
    for i in range(n):
        if(s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u'):
            cv += 1
        else:
            cc += 1
    return(cv, cc)


# main
s = input('Enter word:')
counts(s)
print(counts)
