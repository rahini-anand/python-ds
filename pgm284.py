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
        return (xy, self.__z)


'''
# OOT1
a = a3nos(a=10, b=3)
d = a.dispall()
print(d[0][0])
print(d[0][1])
print(d[1])

# 2
a.setz(100)
a.disp()
b = a.getz()
print(b)

# 3
a.setxyz(110, 111, 112)
c = a.dispall()
print(c[0][0])
print(c[0][1])
print(c[1])

e = a.getxyz()
print(e[0][0])
print(e[0][1])
print(e[1])


# 4
a.reset(1, 2, 5)
f = a.dispall()
print(f[0][0])
print(f[0][1])
print(f[1])
'''
