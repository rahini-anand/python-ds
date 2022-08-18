#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :219
Created on Fri Aug 12 12:19:37 2022
Title: read biodata from kb and write it into 
file
@author: rahini
"""
import pickle
f = open('biodata.dat', 'wb')
a = []
name = input('name:')
age = int(input('age:'))
salary = int(input('salary:'))
address = input('address:')
b = [name, age, salary, address]
a.append(b)
pickle.dump(a, f)
f.close()
