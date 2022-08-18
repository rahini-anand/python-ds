#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :157
Created on Mon Jul 25 00:24:21 2022
Title: construct n students biodata and print
    it person by person
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
for k in a:
    print(k)
