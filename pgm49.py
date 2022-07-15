#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :49
Created on Thu Jul  7 18:21:43 2022
Title: given character is lower case or not
@author: rahini
"""
ch = input('ch=')
x = ord(ch)
if(x >= 97 and x <= 122):
    print("lower case")
else:
    print("not a lower case")
