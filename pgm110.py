#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :110
Created on Fri Jul 22 14:59:05 2022
Title: construct n students biodata and print it
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
print(a)
