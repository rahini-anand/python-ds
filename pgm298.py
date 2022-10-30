#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :298
Created on Mon Oct 17 12:13:22 2022
Title: draw triangle and find its area and perimeter
@author: rahini
"""
from pgm295 import shape


class triangle(shape):
    _b: None
    _h: None
    _a: None

    def draw(self):
        j = 1
        k = 5
        for i in range(5):
            print(' '*k+'*'*j)
            k -= 1
            j += 2

    def area(self, a, b):
        self._b = a
        self._h = b
        area = 1/2*self._b*self._h
        return area

    def perimeter(self, a, b, c):
        self._b = a
        self._h = b
        self._a = c
        p = self._b+self._h+self._a
        return p


# OOT1
a = triangle()
# 2
draw = a.draw()
print(draw)
# 3
ar = a.area(5, 7)
print(ar)
# 4
p = a.perimeter(3, 5, 7)
print(p)
