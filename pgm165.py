#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :165
Created on Mon Jul 25 14:22:10 2022
Title: construct a list of nos from 1 to 100
and add 50 to all the even nos
@author: rahini
"""
a = [i+50 if(i % 2 == 0) else i for i in range(1, 101)]
print(a)
