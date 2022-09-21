#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :270
Created on Mon Sep 19 12:38:16 2022
Title: To find sum of two int nos using closure
function
@author: rahini
"""


def find():
    def sums(a, b):
        x = a+b
        return x
    return sums


# main
x1 = find()
x2 = find()
print(x1(10, 20))
print(x2(5, 2))
