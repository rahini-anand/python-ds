#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :286
Created on Fri Oct  7 12:39:34 2022
Title: access of two nos using protected access
@author: rahini
"""


class a2nospro1():
    _x: None
    _y: None

    def __init__(self, a=10, b=20):
        self._x = a
        self._y = b

    def setx(self, a):
        self._x = a

    def sety(self, b):
        self._y = b

    def setxy(self, a, b):
        self._x = a
        self._y = b

    def reset(self, a, b):
        self._x = a
        self._y = b

    def getx(self):
        return self._x

    def gety(self):
        return self._y

    def getxy(self):
        return self._x, self._y

    def disp(self):
        print(self._x, self._y)


'''
# OOT1
a = a2nospro1()
a.disp()

# OOT2
a.setx(100)
a.disp()
b = a.getx()
print(b)

# OOT3
a.sety(200)
a.disp()
c = a.gety()
print(c)

# OOT4
a.setxy(110, 210)
a.disp()
d = a.getxy()
print(d)

a.reset(1, 2)
a.disp()
'''
