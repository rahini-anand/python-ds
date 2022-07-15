#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :29
Created on Sun Jun 26 14:38:12 2022
Title: given int number single digit, two digit,
        three digit or four digit
@author: rahini
"""
a = int(input('a='))
if(a >= 0 and a <= 9):
    print("single digit")
elif(a >= 10 and a <= 99):
    print("two digit")
elif(a >= 100 and a <= 999):
    print("three digit")
elif(a >= 1000 and a <= 9999):
    print("four digit")
else:
    print("not a four digit")
