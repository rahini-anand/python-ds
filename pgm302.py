#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :302
Created on Tue Oct 18 12:25:43 2022
Title: to perform 9 types of slicing in numpy
array
@author: rahini
"""
import numpy as np
import random
n = int(input('n='))
m = int(input('m='))

l = [random.randint(0, 100) for i in range(20)]
npl = np.array(l)
print(npl)

# 1 first n elements from left
s1 = npl[:n]
print("s1", s1)

# 2 all elements from mth position from left
s2 = npl[m-1:]
print("s2", s2)

# 3 n elements from mth position from left
s3 = npl[m:m+n-1]
print("s3", s3)

# 4 alternate elements from left
s4 = npl[0:19:2]
print("s4", s4)

# 5 reverse the array
s5 = npl[::-1]
print("s5", s5)

# 6 first n elements from right
s6 = npl[-1:-n-1:-1]
print("s6", s6)

# 7 all elements from mth position from right
s7 = npl[-m:-21:-1]
print("s7", s7)

# 8 n elements from mth position from right
s8 = npl[-m:-m-n:-1]
print("s8", s8)

# 9 alternate elements from right
s9 = npl[::-2]
print("s9", s9)
