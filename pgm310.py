#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :310
Created on Sat Oct 22 12:47:08 2022
Title: segregate 50 students based on their
grade
@author: rahini
"""
import numpy as np
import csv
f = open('50s marksheet.csv', 'r')
x = csv.reader(f)
h = next(x)
fcwd = []
fc = []
sc = []
fail = []
for i in x:
    if(i[8] == 'FCWD'):
        fcwd.append(i)
    if(i[8] == 'FC'):
        fc.append(i)
    if(i[8] == 'SC'):
        sc.append(i)
    if(i[8] == 'FAIL'):
        fail.append(i)

f1 = open('fcwd.csv', 'w')
f2 = open('fc.csv', 'w')
f3 = open('sc.csv', 'w')
f4 = open('fail.csv', 'w')

a1 = np.array(fcwd)
a2 = np.array(fc)
a3 = np.array(sc)
a4 = np.array(fail)

a1.tofile("f1")
a2.tofile("f2")
a3.tofile("f3")
a4.tofile("f4")
f.close()
f1.close()
f2.close()
f3.close()
f4.close()
