#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :197
Created on Thu Jul 28 21:14:40 2022
Title: to store roll no and name of 10 students
in dictionary and print it
@author: rahini
"""
d = {}
for i in range(10):
    roll = int(input('r.no:'))
    name = input('name=')
    d[roll] = name
print(d)
