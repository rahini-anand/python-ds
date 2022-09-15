#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :266
Created on Thu Sep 15 12:40:50 2022
Title: find arithmetic operations using decorator
@author: rahini
"""


def sums(a, b):
    x = a+b
    return x


def difference(a, b):
    x = a-b
    return x


def product(a, b):
    x = a*b
    return x


def division(a, b):
    x = a/b
    return x


def mod(a, b):
    x = a % b
    return x


def quotient(a, b):
    x = a // b
    return x


def find(x, a, b):
    print(x(a, b))


# main
find(sums, 20, 5)
find(difference, 15, 5)
find(product, 10, 5)
find(division, 49, 7)
find(mod, 15, 2)
find(quotient, 15, 2)
