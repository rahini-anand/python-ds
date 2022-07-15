#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :34
Created on Sun Jun 26 15:12:38 2022
Title: character is arithmetic, relational or logical
        operator
@author: rahini
"""
ch = input("ch:")
if(ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '%' or ch == '//' or ch == '**'):
    print("arithmetic operator")
elif(ch == '<' or ch == '>' or ch == '=' or ch == '<=' or ch == '>=' or ch == '=='):
    print("realtional operator")
elif(ch == 'and' or ch == 'or' or ch == 'not'):
    print("Logical operator")
else:
    print("not a logical operator")
