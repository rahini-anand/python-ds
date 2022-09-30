#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :276
Created on Thu Sep 22 12:09:12 2022
Title: biggest of 3 nos using constructor in oop
@author: rahini
"""


class b3nos():
    __a: None
    __b: None
    __c: None
    __x = None

    def __init__(self):
        self.__a = 10
        self.__b = 12
        self.__c = 20

    def find(self):
        self.__x = (self.__a if(self.__a > self.__c) else self.__c) if(
            self.__a > self.__b) else (self.__b if(self.__b > self.__c)else self.__c)

    def disp(self):
        print(self.__x)


# oot
a = b3nos()
a.find()
a.disp()
