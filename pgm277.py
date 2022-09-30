#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :277
Created on Sat Sep 24 11:30:57 2022
Title: sum of two nos using default and
keyword arguement using constructor
@author: rahini
"""


class s2nos():
    __a: None
    __b: None
    __s: None

    def __init__(self, x=10, y=20):
        self.__a = x
        self.__b = y

    def find(self):
        self.__s = self.__a+self.__b

    def disp(self):
        print(self.__s)


# oot
a = s2nos()
b = s2nos(12)
c = s2nos(14, 26)
d = s2nos(y=50)
a.find()
b.find()
c.find()
d.find()
a.disp()
b.disp()
c.disp()
d.disp()
