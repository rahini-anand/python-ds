#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :145
Created on Sun Jul 24 13:39:20 2022
Title: find given int is palindrome or not
@author: rahini
"""
no = int(input('no:'))
s1 = str(no)
s2 = ''
n = len(s1)
for i in range(1, n+1):
    s2 += s1[-i]
print(s2)
rno = int(s2)
if(no == rno):
    print("palindrome")
else:
    print("not a palindrome")
