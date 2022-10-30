#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :293
Created on Thu Oct 13 12:23:09 2022
Title: perform arithmetic operations in list
using operator overloading
@author: rahini
"""
from pgm290 import MyList


class MyListScalarPoly(MyList):
    def __init__(self, n=10):
        MyList.__init__(self, n)

    def __add__(self, c):
        x = [i+c for i in self._a]
        return x

    def __sub__(self, c):
        x = [i-c for i in self._a]
        return x

    def __mul__(self, c):
        x = [i*c for i in self._a]
        return x

    def __truediv__(self, c):
        x = [i/c for i in self._a]
        return x

    def __mod__(self, c):
        x = [i % c for i in self._a]
        return x

    def __floordiv__(self, c):
        x = [i//c for i in self._a]
        return x

    def __pow__(self, c):
        x = [i**c for i in self._a]
        return x


# OOT1
a = MyListScalarPoly()
print(a)
# 2
s = a+10
print(s)
# 3
d = a-10
print(d)
# 4
p = a*10
print(p)
# 5
di = a/10
print(di)
# 6
m = a % 10
print(m)
# 7
q = a//10
print(q)
