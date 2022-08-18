#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :162
Created on Mon Jul 25 14:16:13 2022
Title: construct a list of only even nos from
0 to 100 using list comprehension
@author: rahini
"""
a = [i for i in range(101) if(i % 2 == 0)]
print(a)
