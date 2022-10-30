#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :310ds
Created on Wed Oct 26 11:50:04 2022
Title: to segregate 50 students based on their
marks
@author: rahini
"""
import numpy as np
import random
f = open('50s marksheet copy.dat', 'wb')
l = [random.randint(0, 100) for i in range(50)]
a = np.array(l)
print(a)
a.tofile("f")
b1 = a >= 85
b2 = (a >= 65) & (a < 85)
b3 = (a >= 50) & (a < 65)
b4 = a < 50
f1 = open('fcwd.dat', 'wb')
f2 = open('fc.dat', 'wb')
f3 = open('sc.dat', 'wb')
f4 = open('fail.dat', 'wb')
a[b1].tofile("f1")
a[b2].tofile("f2")
a[b3].tofile("f3")
a[b4].tofile("f4")
f.close()
f1.close()
f2.close()
f3.close()
f4.close()
a1 = np.fromfile("f1", dtype=np.int64)
print(a1)
