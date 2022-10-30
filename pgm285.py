#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :285
Created on Fri Oct  7 11:29:18 2022
Title: operations on three nos using a3nos
@author: rahini
"""
from pgm284 import a3nos


class op3nos(a3nos):
    def __init__(self, x, y, z):
        a3nos.__init__(self, x, y, z)

    def sums(self):
        xyz = a3nos.getxyz(self)
        sums = xyz[0][0]+xyz[0][1]+xyz[1]
        return sums

    def sumsq(self):
        x = a3nos.getxyz(self)
        sumsq = (x[0][0]*x[0][0])+(x[0][1]*x[0][1])+(x[1]*x[1])
        return sumsq

    def product(self):
        x = a3nos.getxyz(self)
        product = x[0][1]*x[0][0]*x[1]
        return product

    def big(self):
        x = a3nos.getxyz(self)
        a = x[0][0]
        b = x[0][1]
        c = x[1]
        big = (a if(a > c) else c) if(a > b) else (b if(b > c) else c)
        return big

    def small(self):
        x = a3nos.getxyz(self)
        a = x[0][0]
        b = x[0][1]
        c = x[1]
        small = (a if(a < c) else c) if(a < b) else (b if(b < c) else c)
        return small


# OOT
a = op3nos(x=10, y=20, z=30)
s = a.sums()
print(s)
ss = a.sumsq()
print(ss)
p = a.product()
print(p)
b = a.big()
print(b)
sm = a.small()
print(sm)
