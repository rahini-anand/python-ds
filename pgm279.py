#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :279
Created on Wed Sep 28 11:34:40 2022
Title: find sum of two nos using setter and 
getter function
@author: rahini
"""


class s2nos():
    __a: None
    __b: None
    __s: None

    def __init__(self, x=10, y=20):
        self.__a = x
        self.__b = y

    def seta(self, x):
        self.__a = x

    def setb(self, y):
        self.__b = y

    def setab(self, x, y):
        self.__a = x
        self.__b = y

    def reset(self):
        self.__a = self.__a
        self.__b = self.__b

    def geta(self):
        return self.__a

    def getb(self):
        return self.__b

    def getab(self):
        return self.__a, self.__b

    def gets(self):
        return self.__s

    def find(self):
        self.__s = self.__a+self.__b

    def disp(self):
        print(self.__s)


# oot1
a = s2nos()

a.find()
a.disp()

# oot2
a.seta(100)
b = a.geta()
a.find()
a.disp()

# oot3
a.setb(200)
c = a.getb()
a.find()
a.disp()

# oot4
a.setab(110, 210)
d = a.getab()
a.find()
a.disp()
