#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :31
Created on Sun Jun 26 14:54:28 2022
Title: character is arithmetic operator or not
@author: rahini
"""
ch = input('ch:')
if ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '%' or ch == '//' or ch == '**':
    print("arithmetic operator")
else:
    print("not an arithmetic operator")
