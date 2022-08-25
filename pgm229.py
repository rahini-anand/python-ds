#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :229
Created on Fri Aug 19 11:40:58 2022
Title: print first data vertically
@author: rahini
"""
import csv
f = open('student biodata.csv', 'r')
x = csv.reader(f)
h = next(x)
fd = next(x)
print(fd[0])
print(fd[1])
print(fd[2])
print(fd[3])
print(fd[4])
print(fd[5])
print(fd[6])
print(fd[7])
print(fd[8])
f.close()
