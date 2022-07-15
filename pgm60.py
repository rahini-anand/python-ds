#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :60
Created on Sat Jul  9 13:54:46 2022
Title: print numbers between two limits and find it even or odd
@author: rahini
"""
i = int(input('i='))
j = int(input('j='))
while(i <= j):
    if(i % 2 == 0):
        print(i, "even number")
    else:
        print(i, "odd number")
    i += 1
