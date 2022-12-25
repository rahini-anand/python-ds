#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :379
Created on Thu Dec 22 12:28:14 2022
Title: draw formatted line
@author: rahini
"""
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
y2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
plt.plot(x, y1, 'd-b')
plt.plot(x, y2, '*:r')
plt.show
