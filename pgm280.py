#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :280
Created on Fri Sep 30 12:19:57 2022
Title: access two int nos using setter and 
getter function and constructor
@author: rahini
"""


class a2nos():
    __x: None
    __y: None

    def __init__(self, a=10, b=20):
        self.__x = a
        self.__y = b

    def setx(self, a):
        self.__x = a

    def sety(self, b):
        self.__y = b

    def setxy(self, a, b):
        self.__x = a
        self.__y = b

    def reset(self):
        self.__x = self.__x
        self.__y = self.__y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def getxy(self):
        return self.__x, self.__y

    def disp(self):
        print(self.__x)
        print(self.__y)


# OOT1
a = a2nos()
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
