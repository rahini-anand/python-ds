#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :268
Created on Mon Sep 19 12:12:41 2022
Title: find biggest of three nos using inner
function
@author: rahini
"""


def find(a, b, c):
    def bot():
        x = (a if(a > c)else c) if(a > b) else(b if (b > c) else c)
        return x
    x = bot()
    print(x)


# main
find(5, 10, 2)
