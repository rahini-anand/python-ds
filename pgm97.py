#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :97
Created on Thu Jul 14 13:26:33 2022
Title: to construct a list of ten int nos and
        print it in reverse or negative index
@author: rahini
"""
a = []
i = 0
while(i < 10):
    x = int(input('x='))
    a.append(x)
    i += 1
i = 1
while(i <= 10):
    print(a[-i])
    i += 1
