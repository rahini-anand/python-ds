#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :267
Created on Mon Sep 19 12:10:32 2022
Title: find sum of two int nos using inner 
function
@author: rahini
"""


def find(a, b):
    def sum():
        x = a+b
        return x
    x = sum()
    print(x)


# main
find(10, 20)
