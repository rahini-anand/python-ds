#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :297
Created on Mon Oct 17 12:08:40 2022
Title: draw square and find its area and perimeter
@author: rahini
"""
from pgm295 import shape


class square(shape):
    _a: None

    def draw(self, n):
        for i in range(n):
            print('*'*n)

    def area(self, a):
        self._a = a
        area = self._a*self._a
        return area

    def perimeter(self, a):
        self._a = a
        p = 4*self._a
        return p


# OOT1
a = square()
# 2
draw = a.draw(5)
print(draw)
# 3
ar = a.area(4)
print(ar)
# 4
p = a.perimeter(3)
print(p)
