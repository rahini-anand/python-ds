#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :265
Created on Thu Sep 15 12:26:10 2022
Title: find sum of two nos using decorators
@author: rahini
"""


def sum(a, b):
    x = a+b
    return x


def find(x, a, b):
    print(x(a, b))


# main
find(sum, 10, 20)
