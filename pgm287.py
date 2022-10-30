#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :287
Created on Sat Oct  8 11:29:07 2022
Title: operation on two nos using protected access
@author: rahini
"""
from pgm286 import a2nospro1


class op2nospro(a2nospro1):
    def sums(self):
        s = self._x+self._y
        return s

    def difference(self):
        d = self._x-self._y
        return d

    def product(self):
        p = self._x*self._y
        return p

    def division(self):
        di = self._x/self._y
        return di

    def mod(self):
        m = self._x % self._y
        return m

    def quotient(self):
        q = self._x//self._y
        return q

    def big(self):
        big = self._x if(self._x > self._y) else self._y
        return big

    def small(self):
        small = self._x if(self._x < self._y) else self._y
        return small


# OOT
a = op2nospro()
s = a.sums()
print(s)
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
big = a.big()
print(big)
small = a.small()
print(small)
