#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :40
Created on Sun Jun 26 15:33:18 2022
Title: leap year or not using not operator
@author: rahini
"""
x = int(input('Enter year:'))
if not x % 4:
    print("leap year")
else:
    print("not a leap year")
