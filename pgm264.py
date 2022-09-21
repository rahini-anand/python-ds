#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :264
Created on Tue Sep 20 13:44:29 2022
Title: to construct n students biodata and 
print it in funciton
@author: rahini
"""


def bio(a):
    for i in a:
        print(i)


# main
n = int(input('n='))
a = []
for i in range(n):
    b = []
    name = input('name:')
    age = int(input('age:'))
    address = input('address:')
    emailid = input('email id:')
    b = [name, age, address, emailid]
    a.append(b)
bio(a)
