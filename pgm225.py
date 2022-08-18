#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :225
Created on Thu Aug 18 11:24:21 2022
Title: load the entire csv file and open it
@author: rahini
"""
import csv
f = open('student biodata.csv', 'r')
x = csv.reader(f)
for i in x:
    print(i)
f.close()
