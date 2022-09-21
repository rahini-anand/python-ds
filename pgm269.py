#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :269
Created on Mon Sep 19 12:14:28 2022
Title: find 6 arithmetic operations using inner
fucntion and simplecal o.fn.
@author: rahini
"""


def simplecal(a, b, opr):
    def sums():
        x = a+b
        return x

    def difference():
        x = a-b
        return x

    def product():
        x = a*b
        return x

    def division():
        x = a/b
        return x

    def remainder():
        x = a % b
        return x

    def quotient():
        x = a//b
        return x
    if(opr == '+'):
        return sums()
    if(opr == '-'):
        return difference()
    if(opr == '*'):
        return product()
    if(opr == '/'):
        return division()
    if(opr == '%'):
        return remainder()
    if(opr == '//'):
        return quotient()


# main
x1 = simplecal(10, 20, '+')
print(x1)
x2 = simplecal(20, 5, '-')
print(x2)
x3 = simplecal(3, 5, '*')
print(x3)
x4 = simplecal(49, 7, '/')
print(x4)
x5 = simplecal(25, 2, '%')
print(x5)
x6 = simplecal(15, 3, '//')
print(x6)
