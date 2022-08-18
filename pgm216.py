#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :216
Created on Tue Aug  9 12:31:58 2022
Title: to load list from file and display it
@author: rahini
"""
import pickle
f = open('list.dat', 'rb')
x = pickle.load(f)
print(x)
f.close()
