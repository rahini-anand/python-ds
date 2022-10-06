#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :281
Created on Sat Oct  1 11:50:42 2022
Title: access two int nos from previous pgm
using point
@author: rahini
"""
from pgm280 import a2nos


class point(a2nos):
    pass


# OOT1
a = point()
a.disp()

# OOT2
a.setx(100)
a.disp()
b = a.getx()
print(b)

# OOT3
a.sety(200)
a.disp()
c = a.gety()
print(c)

# OOT4
a.setxy(110, 210)
a.disp()
d = a.getxy()
print(d)

# OOT5
a.reset()
a.disp()
