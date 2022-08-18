#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :227
Created on Thu Aug 18 13:27:41 2022
Title: to print rows in a vertival column
@author: rahini
"""
import csv
f = open('student biodata.csv', 'r')
x = csv.reader(f)
h = next(x)
rno = []
name = []
age = []
address = []
tamil = []
english = []
maths = []
science = []
ss = []
for j in x:
    rno.append(j[0])
    name.append(j[1])
    age.append(j[2])
    address.append(j[3])
    tamil.append(j[4])
    english.append(j[5])
    maths.append(j[6])
    science.append(j[7])
    ss.append(j[8])
print(h[0], rno)
print(h[1], name)
print(h[2], age)
print(h[3], address)
print(h[4], tamil)
print(h[5], english)
print(h[6], maths)
print(h[7], science)
print(h[8], ss)
f.close()
