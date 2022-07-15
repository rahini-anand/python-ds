#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :17
Created on Sun Jun 19 13:28:50 2022
Title: reverse three digit number
@author: rahini
"""
a = int(input('a='))
r1 = a % 10  # 1thplace
q1 = a//10
r2 = q1 % 10  # 10th place
q2 = q1//10  # 100th place
u = (r1*100)+(r2*10)+q2
print(u)
