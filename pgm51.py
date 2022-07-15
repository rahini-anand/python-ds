#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :51
Created on Sat Jul  9 13:32:03 2022
Title: to find a given character is upper,lower,digit or
        special character
@author: rahini
"""
ch = input('ch:')
x = ord(ch)
if(x >= 65 and x <= 90):
    print("upper case")
elif(x >= 97 and x <= 122):
    print("lower case")
elif(x >= 48 and x <= 57):
    print("digit")
else:
    print("special character")
