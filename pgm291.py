#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :291
Created on Tue Oct 11 12:14:55 2022
Title: perform arithmetic operations on Mylist
@author: rahini
"""
from pgm290 import MyList


class MyListScalar(MyList):
    def __init__(self, n=10):
        MyList.__init__(self, n)

    def sums(self, c):
        s = [i+c for i in self._a]
        return s

    def difference(self, c):
        d = [i-c for i in self._a]
        return d

    def product(self, c):
        p = [i*c for i in self._a]
        return p

    def division(self, c):
        di = [i/c for i in self._a]
        return di

    def mod(self, c):
        m = [i % c for i in self._a]
        return m

    def quotient(self, c):
        q = [i//c for i in self._a]
        return q


# OOT1
a = MyListScalar()
print(a)
# 2
s = a.sums(5)
print(s)
# 3
d = a.difference(5)
print(d)
# 4
p = a.product(10)
print(p)
# 5
di = a.division(2)
print(di)
# 6
m = a.mod(2)
print(m)
# 7
q = a.quotient(2)
print(q)
