#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :224
Created on Tue Aug 16 11:41:24 2022
Title: display the people only in a particular
age
@author: rahini
"""
import pickle
try:
    f = open('biodata.dat', 'rb')
    x = pickle.load(f)
    while(x):
        if(x[1] == 29):
            print(x)
        x = pickle.load(f)
except:
    pass
f.close()
