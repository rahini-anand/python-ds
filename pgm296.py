#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :296
Created on Mon Oct 17 11:39:45 2022
Title: to draw rectangle and find its area and
perimeter
@author: rahini
"""
from pgm295 import shape


class rectangle(shape):
    _l: None
    _b: None

    def draw(self, n):
        for i in range(n):
            print('*'*(n-1))

    def area(self, a, b):
        self._l = a
        self._b = b
        a = self._l*self._b
        return a

    def perimeter(self, a, b):
        self._l = a
        self._b = b
        p = 2*(self._l+self._b)
        return p


# OOT1
a = rectangle()
# 2
r = a.draw(5)
print(r)
# 3
ar = a.area(5, 4)
print(ar)
# 4
p = a.perimeter(3, 2)
print(p)
