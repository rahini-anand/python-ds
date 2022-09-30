#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :275
Created on Thu Sep 22 11:56:53 2022
Title: find sum of two nos using constructor 
in oop
@author: rahini
"""


class s2nos():
    __a: None
    __b: None
    __s: None

    def __init__(self):
        self.__a = 10
        self.__b = 20

    def find(self):
        self.__s = self.__a+self.__b

    def disp(self):
        print(self.__s)


# oot
a = s2nos()
a.find()
a.disp()
