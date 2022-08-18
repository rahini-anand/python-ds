#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :198
Created on Thu Jul 28 21:22:28 2022
Title: 
@author: rahini
"""
d = {}
n = int(input('n='))
for i in range(n):
    roll = int(input('r.no:'))
    name = input('name=')
    d[roll] = name
for i in d:
    print(i, d[i])
