#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :288
Created on Sat Oct  8 12:15:46 2022
Title: to access three nos using protected access
@author: rahini
"""
from pgm286 import a2nospro1


class a3nospro(a2nospro1):
    _z: None

    def __init__(self, a, b, c):
        a2nospro1.__init__(self, a, b)
        self._z = c

    def setz(self, c):
        self._z = c

    def setxyz(self, a, b, c):
        self._x = a
        self._y = b
        self._z = c

    def reset(self, a, b, c):
        self._x = a
        self._y = b
        self._z = c

    def getz(self):
        return self._z

    def getxyz(self):
        return self._x, self._y, self._z

    def disp(self):
        print(self._z)

    def dispall(self):
        print(self._x, self._y, self._z)


'''
# OOT
a = a3nospro(a=10, b=20, c=30)
a.dispall()
# 2
a.setz(100)
a.dispall()
b = a.getz()
print(b)
# 3
a.setxyz(a=100, b=200, c=300)
a.dispall()
c = a.getxyz()
print(c)
# 4
a.reset(a=1, b=2, c=3)
a.dispall()
'''
