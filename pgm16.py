#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :16
Created on Sun Jun 19 13:22:49 2022
Title: find digits of three digit
number
@author: rahini
"""
a = int(input('a=?'))
r1 = a % 10
q1 = a//10
r2 = q1 % 10
q2 = q1//10
print(q1, q2, r1)
