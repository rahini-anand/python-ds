#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :48
Created on Thu Jul  7 18:15:47 2022
Title: given character is upper or not
@author: rahini
"""
ch = input("ch=")
x = ord(ch)
if(x >= 65 and x <= 90):
    print("upper case")
else:
    print("not an upper case")
