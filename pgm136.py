#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :136
Created on Sun Jul 24 13:00:32 2022
Title: print hollow triangle
@author: rahini
"""
print(' '*6+'*')
k = 5
j = 1
for i in range(1, 6):
    print(' '*k+'*'+' '*j+'*')
    k -= 1
    j += 2
print(('*'+' ')*6+'*')
