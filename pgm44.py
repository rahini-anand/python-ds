#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :44
Created on Thu Jul  7 18:00:41 2022
Title: smallest of three numbers
@author: rahini
"""
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
small = a if(a < b) else b
small = small if(small < c) else c
print(small)
