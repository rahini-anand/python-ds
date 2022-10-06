#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :
Created on Mon Oct  3 11:55:53 2022
Title: 
@author: rahini
"""
from pgm280 import a2nos


class op2nos(a2nos):
    def sums(self):
        x = a2nos.getx(self)
        y = a2nos.gety(self)
        s = x+y
        return s


# OOT
a = op2nos()
s = a.sums()
print(s)
