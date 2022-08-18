#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :163
Created on Mon Jul 25 14:18:01 2022
Title: construct a list of nos i.e. divisible 
by 3,5and7 from 0 to 100
@author: rahini
"""
a = [i for i in range(101) if(i % 3 == 0 and i % 5 == 0 and i % 7 == 0)]
print(a)
