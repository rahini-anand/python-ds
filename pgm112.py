#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :112
Created on Fri Jul 22 15:07:13 2022
Title: construct n students biodata print only
        name,address and email id
@author: rahini
"""
a = []
i = 0
n = int(input('n:'))
while(i < n):
    b = []
    name = input('name:')
    age = input('age:')
    address = input('address:')
    email = input('mail ad:')
    b = [name, age, address, email]
    a.append(b)
    i += 1
i = 0
while(i < n):
    print(a[i][0])
    print(a[i][2])
    print(a[i][3])
    i += 1
