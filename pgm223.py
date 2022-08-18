#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :223
Created on Sat Aug 13 12:29:09 2022
Title: display only name and address fron file
@author: rahini
"""
import pickle
try:
    f = open('biodata.dat', 'rb')
    x = pickle.load(f)
    while(x):
        print(x[0])
        print(x[3])
        x = pickle.load(f)
except:
    pass
f.close()
