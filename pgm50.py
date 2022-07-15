#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :50
Created on Thu Jul  7 18:24:02 2022
Title: given character digit or not
@author: rahini
"""
ch = input('ch=')
x = ord(ch)
if(x >= 48 and x <= 57):
    print("single digit")
else:
    print("not a digit")
