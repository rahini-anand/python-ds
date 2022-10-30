#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :292
Created on Tue Oct 11 12:46:49 2022
Title: perform arithmetic (vector) operations in Mylist
@author: rahini
"""
from pgm290 import MyList
import random


class MyListVector(MyList):
    def __init__(self, n=10):
        MyList.__init__(self, n)

    def sums(self, b, n):
        a = self._a
        s = [a[i]+b[i] for i in range(n)]
        return s

    def difference(self, b, n):
        a = self._a
        d = [a[i]-b[i] for i in range(n)]
        return d

    def product(self, b, n):
        a = self._a
        p = [a[i]*b[i] for i in range(n)]
        return p

    def division(self, b, n):
        a = self._a
        di = [a[i]*b[i] for i in range(n)]
        return di

    def mod(self, b, n):
        a = self._a
        m = [a[i] % b[i] for i in range(n)]
        return m

    def quotient(self, b, n):
        a = self._a
        q = [a[i]//b[i] for i in range(n)]
        return q


# OOT1
a = MyListVector()
print(a)
b = [random.randint(0, 100) for x in range(10)]
print(b)
# 2
s = a.sums(b, 10)
print(s)
# 3
d = a.difference(b, 10)
print(d)
# 4
p = a.product(b, 10)
print(p)
# 5
di = a.division(b, 10)
print(di)
# 6
m = a.mod(b, 10)
print(m)
# 7
q = a.quotient(b, 10)
print(q)
