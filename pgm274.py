#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :274
Created on Wed Sep 21 22:57:33 2022
Title: find biggest of 3 int nos using oop
@author: rahini
"""


class b3nos():
    __a: None
    __b: None
    __c: None
    __x: None

    def sets(self):
        self.__a = 10
        self.__b = 20
        self.__c = 3

    def find(self):
        self.__x = (self.__a if(self.__a > self.__c) else self.__c) if(
            self.__a > self.__b) else (self.__b if(self.__b > self.__c)else self.__c)

    def disp(self):
        print(self.__x)


# oot
a = b3nos()
a.sets()
a.find()
a.disp()
