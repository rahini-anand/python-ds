#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :26
Created on Sun Jun 26 14:26:02 2022
Title: given three digit number is 
        palindrome or not
@author: rahini
"""
n = int(input("n:"))
r1 = n % 10  # 1st digit
q1 = n//10
r2 = q1 % 10  # 2nd digit
q2 = q1//10  # 3rd digit
u = (r1*100)+(r2*10)+q2
if(n == u):
    print("number is palindrome")
else:
    print("number is not a palindrome")
