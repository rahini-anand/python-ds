#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :354
Created on Mon Dec  5 11:55:46 2022
Title: to perform various built in functions in pandas
@author: rahini
"""
import pandas as pd
import random
n = [random.randint(10, 100) for i in range(20)]
s = pd.Series(n)
print(s)

# first n elements
f = s.head(7)
print("head", f)

# last n elements
l = s.tail(7)
print("tail", l)

# largest no of first n elements
l1 = s.nlargest(10)
print("largest", l1)

# smallest of first n elements
s1 = s.nsmallest(10)
print("smallest", s1)

# mean of elements
m = s.mean()
print("mean", m)

# sum of elements
s2 = s.sum()
print("sum", s2)

# product of elements
p = s.product()
print("product", p)

# maximum element
m1 = s.max()
print("max", m1)

# minimum element
m2 = s.min()
print("minimum", m2)

# median
m3 = s.median()
print("median", m3)
