#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :294
Created on Fri Oct 14 11:49:39 2022
Title: perform arithmetic operations on two lists
(vetor) using operator overloading
@author: rahini
"""
import random
from pgm290 import MyList


class MyListVectorPoly(MyList):
    def __init__(self, n=10):
        MyList.__init__(self, n)

    def __add__(self, b):
        a = self._a
        n = 10
        x = [a[i]+b[i] for i in range(n)]
        return x

    def __sub__(self, b):
        a = self._a
        n = 10
        x = [a[i]-b[i] for i in range(n)]
        return x

    def __mul__(self, b):
        a = self._a
        n = 10
        x = [a[i]*b[i] for i in range(n)]
        return x

    def __truediv__(self, b):
        a = self._a
        n = 10
        x = [a[i]/b[i] for i in range(n)]
        return x

    def __mod__(self, b):
        a = self._a
        n = 10
        x = [a[i] % b[i] for i in range(n)]
        return x

    def __floordiv__(self, b):
        a = self._a
        n = 10
        x = [a[i]//b[i] for i in range(n)]
        return x


# OOT1
a = MyListVectorPoly()
print(a)
# 2
b = [random.randint(0, 100) for i in range(10)]
print(b)
# 3
x = a+b
print(x)
# 4
s = a-b
print(s)
# 5
m = a*b
print(m)
# 6
d = a/b
print(d)
# 7
mo = a % b
print(mo)
# 8
fd = a//b
print(fd)
