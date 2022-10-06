#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :283
Created on Mon Oct  3 12:25:05 2022
Title: to perform operations on two int nos
@author: rahini
"""
from pgm280 import a2nos


class op2nos(a2nos):
    def difference(self):
        x = a2nos.getx(self)
        y = a2nos.gety(self)
        d = x-y
        return d

    def product(self):
        x = a2nos.getx(self)
        y = a2nos.gety(self)
        p = x*y
        return p

    def division(self):
        x = a2nos.getx(self)
        y = a2nos.gety(self)
        di = x/y
        return di

    def mod(self):
        x = a2nos.getx(self)
        y = a2nos.gety(self)
        m = x % y
        return m

    def quotient(self):
        x = a2nos.getx(self)
        y = a2nos.gety(self)
        q = x//y
        return q

    def big(self):
        x = a2nos.getx(self)
        y = a2nos.gety(self)
        b = x if(x > y) else y
        return b

    def small(self):
        x = a2nos.getx(self)
        y = a2nos.gety(self)
        s = x if(x < y) else y
        return s


# OOT
a = op2nos()
d = a.difference()
print(d)
p = a.product()
print(p)
di = a.division()
print(di)
m = a.mod()
print(m)
q = a.quotient()
print(q)
b = a.big()
print(b)
s = a.small()
print(s)
