#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :42
Created on Thu Jul  7 17:56:31 2022
Title: smallest of two integer using ternary expression
@author: rahini
"""
a = int(input('a:'))
b = int(input('b:'))
small = a if(a < b) else b
print(small)
