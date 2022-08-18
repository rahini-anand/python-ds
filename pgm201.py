#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :201
Created on Mon Aug  1 11:28:44 2022
Title: display a program file on a screen
@author: rahini
"""
f = open('test.txt', 'r')
x = f.read()
print(x)
f.close()
