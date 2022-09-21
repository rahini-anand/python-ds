#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :271
Created on Tue Sep 20 11:47:24 2022
Title: perform arithmetic operations using 
closure function
@author: rahini
"""


def find(opr):
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

    def remainder(a, b):
        x = a % b
        return x

    def quotient(a, b):
        x = a//b
        return x

    if(opr == '+'):
        return sums
    elif(opr == '-'):
        return difference
    elif(opr == '*'):
        return product
    elif(opr == '/'):
        return division
    elif(opr == '%'):
        return remainder
    elif(opr == '//'):
        return quotient


# main
x1 = find('+')
print(x1(20, 10))
x2 = find('-')
print(x2(20, 10))
x3 = find('*')
print(x3(20, 10))
x4 = find('/')
print(x4(20, 10))
x5 = find('%')
print(x5(20, 10))
x6 = find('//')
print(x6(20, 10))
