#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :53
Created on Sat Jul  9 13:39:17 2022
Title: convert lower case to upper case
@author: rahini
"""
ch = input('ch:')
x = ord(ch)
if(x >= 95 and x <= 122):
    ch = chr(x-32)
else:
    ch = chr(x)
print(ch)
