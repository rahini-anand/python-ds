#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :164
Created on Mon Jul 25 14:20:22 2022
Title: construct a list of 0 to 100 and make 
all the even nos zero
@author: rahini
"""
a = [0 if(i % 2 == 0) else i for i in range(101)]
print(a)
