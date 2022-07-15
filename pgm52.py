#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :52
Created on Sat Jul  9 13:35:22 2022
Title: convert upper case to lower case
@author: rahini
"""
ch = input('ch:')
x = ord(ch)
if(x >= 65 and x <= 90):
    ch = chr(x+32)
else:
    ch = chr(x)
print(ch)
