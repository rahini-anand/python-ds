#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :272
Created on Wed Sep 21 12:28:53 2022
Title: to find sum of two int nos using oops
@author: rahini
"""


class s2nos():
    __a: None
    __b: None
    __s: None

    def sets(self):
        self.__a = 10
        self.__b = 20

    def find(self):
        self.__s = self.__a+self.__b

    def disp(self):
        print(self.__s)


# oot
a = s2nos()
a.sets()
a.find()
a.disp()
