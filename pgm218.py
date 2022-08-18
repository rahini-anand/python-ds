#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :218
Created on Fri Aug 12 12:02:32 2022
Title: segregate a single digit, two digit and 
three digit in a diffrent files
@author: rahini
"""
import pickle
f1 = open('list.dat', 'rb')
x = pickle.load(f1)
s = []
t = []
th = []
print(x)
for i in x:
    if(i >= 0 and i <= 9):
        b = [i]
        s.append(b)
    elif(i >= 10 and i <= 99):
        b = [i]
        t.append(b)
    elif(i >= 100 and i <= 999):
        b = [i]
        th.append(b)
print(s)
print(t)
print(th)
f2 = open('single seg.dat', 'wb')
f3 = open('two seg.dat', 'wb')
f4 = open('three seg.dat', 'wb')
pickle.dump(s, f2)
pickle.dump(t, f3)
pickle.dump(th, f4)
f1.close()
f2.close()
f3.close()
f4.close()
