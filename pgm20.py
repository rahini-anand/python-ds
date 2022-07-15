#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :20
Created on Sun Jun 19 13:42:34 2022
Title: find the given integer 
        positive,negative or zero
@author: rahini
"""
n = int(input('n='))
if n > 0:
    print("positive no")
else:
    if n < 0:
        print("negative no")
    else:
        print("zero")
