#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :231
Created on Fri Aug 19 12:21:04 2022
Title: display data in mark sheet format
@author: rahini
"""
import csv
f = open('student biodata.csv', 'r')
x = csv.reader(f)
h = next(x)
for i in x:
    print('          ORCHARD SCHOOL')
    print('             TRICHY')
    print(h[0], ':', i[0])
    print(h[1], '    :', i[1])
    print('SUBJECT', '        MARKS')
    print(h[4], '         :', i[4])
    print(h[5], '       :', i[5])
    print(h[6], '   :', i[6])
    print(h[7], '       :', i[7])
    print(h[8], ':', i[8])
    print(h[9], i[9])
    print()
    ip = input('')
f.close()
