#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :221
Created on Sat Aug 13 11:49:04 2022
Title: read more than one biodata(until stop 
name) and write it to file
@author: rahini
"""
import pickle
f = open('biodata.dat', 'wb')
name = input('name:')
while(name != 'stop'):
    age = int(input('age:'))
    salary = int(input('salary:'))
    address = input('address:')
    b = [name, age, salary, address]
    pickle.dump(b, f)
    name = input('name:')
f.close()
