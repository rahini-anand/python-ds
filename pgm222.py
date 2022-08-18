#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :222
Created on Sat Aug 13 11:54:22 2022
Title: read biodata from file and display it 
one by one
@author: rahini
"""
import pickle
try:
    f = open('biodata.dat', 'rb')
    x = pickle.load(f)
    while(x):
        print(x)
        x = pickle.load(f)
except:
    pass
f.close()
