#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :290
Created on Mon Oct 10 12:21:59 2022
Title: construct list and print it by overloading 
mehtod
@author: rahini
"""
import random


class MyList():
    _a: None

    def __init__(self, n=10):
        self._a = [random.randint(0, 100) for x in range(n)]

    def __str__(self):
        x = ','.join(map(str, self._a))
        return x


'''
# OOT
a = MyList()
print(a)
'''
