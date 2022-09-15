#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :247
Created on Mon Sep  5 11:46:30 2022
Title: find area of cirle,vol of sphere, vol of
cylinder,area of triangle, biggest of 3nos,
smallest of 3nos
@author: rahini
"""
def ac(r1): return 3.14*r1*r1
def vs(r2): return 4/3*3.14*r2*r2*r2


def vc(r3, h1): return 3.14*r3*r3*h1
def at(b, h2): return 1/2*b*h2


def bot(a, b, c): return (a if(a > c)else c)if (a > b)else(b if(b > c)else c)
def sot(a, b, c): return (a if(a < c)else c)if(a < b)else (b if(b < c)else c)


# main
f1 = ac(5)
print("ac", f1)
f2 = vs(6)
print("vs", f2)
f3 = vc(7, 4)
print("vc", f3)
f4 = at(10, 3)
print("at", f4)
f5 = bot(10, 15, 18)
print("bot", f5)
f6 = sot(20, 25, 28)
print("sot", f6)
