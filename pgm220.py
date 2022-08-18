#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :220
Created on Sat Aug 13 11:18:53 2022
Title: read biodata from file and display it
@author: rahini
"""
import pickle
f = open('biodata.dat', 'rb')
x = pickle.load(f)
print(x)
f.close()
