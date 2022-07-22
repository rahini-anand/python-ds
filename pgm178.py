#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :178
Created on Fri Jul 22 15:10:35 2022
Title: data extraction using slicing
@author: rahini
"""
n = int(input('n='))
a = [int(input('no:')) for i in range(n)]
noe = int(input('noe:'))
m = int(input('m='))
# copy first N elements from left
print(a[:noe])
# all elements from mth position from left
print(a[m-1:])
# n elements from mth position
print(a[m-1:m+noe-1])
# alternate elements from left
print(a[0:n:2])
# reverse the element
print(a[::-1])
# fist N elements from right
print(a[:noe:-1])
# all elements from mth position
print(a[m:n:-1])
# N elements from mth position
print(a[m:m+noe:-1])
# alternate elements from right
print(a[::-2])
