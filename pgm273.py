#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :273
Created on Wed Sep 21 22:56:29 2022
Title: find product of 2 int nos using oop
@author: rahini
"""


class p2nos():
    __a: None
    __b: None
    __p: None

    def sets(self):
        self.__a = 10
        self.__b = 20

    def find(self):
        self.__p = self.__a*self.__b

    def disp(self):
        print(self.__p)


# oot
a = p2nos()
a.sets()
a.find()
a.disp()
