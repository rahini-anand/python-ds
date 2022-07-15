#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :45
Created on Thu Jul  7 18:02:51 2022
Title: biggest of three numbers using nested ternary expression
@author: rahini
"""
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
big = (a if(a > c) else c) if (a > b) else (b if(b > c) else c)
print(big)
