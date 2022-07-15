#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :62
Created on Sat Jul  9 14:00:12 2022
Title: read numbers other than 1000 and find it positive, 
        negative or zero
@author: rahini
"""
x = int(input('x:'))
while(x != 1000):
    if(x > 0):
        print("positive")
    elif(x < 0):
        print("negative")
    else:
        print("zero")
    x = int(input('x:'))
