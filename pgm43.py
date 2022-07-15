#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :43
Created on Thu Jul  7 17:58:19 2022
Title: biggest of three integer numbers
@author: rahini
"""
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
big = a if(a > b) else b
big = big if(big > c) else c
print(big)
