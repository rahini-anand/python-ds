#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :232
Created on Mon Aug 22 12:17:51 2022
Title: To display marksheet with result
@author: rahini
"""
import csv
f = open('student biodata.csv', 'r')
x = csv.reader(f)
h = next(x)
result = 'pass'
for i in x:
    print('          ORCHARD SCHOOL')
    print('             TRICHY')
    print(h[0], ':', i[0])
    print(h[1], '    :', i[1])
    print('SUBJECT', '          MARKS', '    RESULT')
    if(int(i[4]) >= 35):
        result = 'pass'
    else:
        result = 'fail'
    print(h[4], '         :   ', i[4], '        ', result)
    if(int(i[5]) >= 35):
        result = 'pass'
    else:
        result = 'fail'
    print(h[5], '       :   ', i[5], '        ', result)
    if(int(i[6]) >= 35):
        result = 'pass'
    else:
        result = 'fail'
    print(h[6], '   :   ', i[6], '       ', result)
    if(int(i[7]) >= 35):
        result = 'pass'
    else:
        result = 'fail'
    print(h[7], '       :   ', i[7], '       ', result)
    if(int(i[8]) >= 35):
        result = 'pass'
    else:
        result = 'fail'
    print(h[8], ':   ', i[8], '       ', result)
    ip = input('')
f.close()
