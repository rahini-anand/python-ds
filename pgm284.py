#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :284
Created on Thu Oct  6 11:29:03 2022
Title: to access three nos
@author: rahini
"""
from pgm280 import a2nos


class a3nos(a2nos):
    __z: None

    def __init__(self, a, b, c=3):
        a2nos.__init__(self, a, b)
        self.__z = c

    def setz(self, c):
        self.__z = c

    def setxyz(self, a, b, c):
        a2nos.setxy(self, a, b)
        self.__z = c

    def reset(self, a, b, c):
        a2nos.reset(self, a, b)
        self.__z = c

    def getz(self):
        return self.__z

    def getxyz(self):
        xy = a2nos.getxy(self)
        return xy, self.__z

    def disp(self):
        print(self.__z)

    def dispall(self):
        xy = a2nos.getxy(self)
        print(xy, self.__z)


# OOT1
a = a3nos(a=10, b=3)
a.dispall()

# 2
a.setz(100)
a.disp()
b = a.getz()
print(b)

# 3
a.setxyz(110, 111, 112)
a.dispall()
a.getxyz()
a.dispall()

# 4
a.reset(1, 2, 5)
a.dispall()
