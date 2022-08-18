#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :190
Created on Thu Jul 28 20:57:05 2022
Title: construct two sets of int nos and find 
its union, intersection and difference
@author: rahini
"""
import random
n = int(input('n='))
a = [random.randint(0, 100) for x in range(n)]
b = [random.randint(0, 100) for y in range(n)]
s1 = set(a)
s2 = set(b)
su = s1.union(s2)
print("su", su)
si = s1.intersection(s2)
print("si", si)
sd = s1.difference(s2)
print(sd, "sd")
