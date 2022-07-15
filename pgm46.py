#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :46
Created on Thu Jul  7 18:06:20 2022
Title: smallest of three nos using nested ternary expression
@author: rahini
"""
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
small = (a if(a < c) else c) if(a < b) else (b if(b < c) else c)
print(small)
