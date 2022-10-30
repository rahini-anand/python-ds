#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :289
Created on Mon Oct 10 11:56:57 2022
Title: perform operations on three nos using protected
@author: rahini
"""
from pgm288 import a3nospro


class op3nospro(a3nospro):
    def __init__(self, a=10, b=20, c=30):
        a3nospro.__init__(self, a, b, c)

    def sums(self):
        s = self._x+self._y+self._z
        return s

    def sumsq(self):
        x = self._x
        y = self._y
        z = self._z
        ss = (x*x)+(y*y)+(z*z)
        return ss

    def product(self):
        p = self._x*self._y*self._z
        return p

    def big(self):
        a = self._x
        b = self._y
        c = self._z
        big = (a if(a > c) else c) if(a > b) else (b if(b > c) else c)
        return big

    def small(self):
        a = self._x
        b = self._y
        c = self._z
        small = (a if(a < c) else c) if(a < b) else (b if(b < c) else c)
        return small


# OOT
a = op3nospro()
s = a.sums()
print(s)
ss = a.sumsq()
print(ss)
p = a.product()
print(p)
big = a.big()
print(big)
sm = a.small()
print(sm)
