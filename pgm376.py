#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :376
Created on Thu Dec 22 11:53:32 2022
Title: draw plot of month vs temperature
@author: rahini
"""
import matplotlib.pyplot as plt
x = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
     'August', 'September', 'October', 'November', 'December']
y = [37, 36, 39, 40, 41, 39, 36, 35, 36, 34, 28, 24]
plt.plot(x, y)
plt.show()
