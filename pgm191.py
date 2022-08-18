#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :191
Created on Thu Jul 28 21:02:49 2022
Title: print the unique values in the list of
n random nos
@author: rahini
"""
n = int(input('n='))
a = [int(input('x=')) for x in range(n)]
s = set(a)
print(s)
