#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :158
Created on Mon Jul 25 00:34:31 2022
Title: construct n students biodata and print
    only name and email id
@author: rahini
"""
a = []
n = int(input('n='))
for i in range(n):
    b = []
    name = input('name:')
    age = int(input('age:'))
    address = input('address:')
    email = input('email:')
    b = [name, age, address, email]
    a.append(b)
for i in range(n):
    print(a[i][0])
    print(a[i][3])
