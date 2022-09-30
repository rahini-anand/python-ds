#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :
Created on Sat Sep 24 11:35:40 2022
Title: 
@author: rahini
"""


class b3nos():
    __a: None
    __b: None
    __c: None
    __big: None

    def __init__(self, x=10, y=12, z=14):
        self.__a = x
        self.__b = y
        self.__c = z

    def find(self):
        self.__big = (self.__a if(self.__a > self.__c) else self.__c) if(
            self.__a > self.__b) else (self.__b if(self.__b > self.__c)else self.__c)

    def disp(self):
        print(self.__big)


# oot
a = b3nos()
b = b3nos(20, 30)
c = b3nos(40)
d = b3nos(y=50, z=60)
a.find()
b.find()
c.find()
d.find()
a.disp()
b.disp()
c.disp()
d.disp()
