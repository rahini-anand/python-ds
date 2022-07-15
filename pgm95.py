#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :95
Created on Tue Jul 12 15:30:28 2022
Title: given integer palindrome or not
@author: rahini
"""
no = int(input('no:'))
s1 = str(no)
s2 = ''
n = len(s1)
i = 1
while(i <= n):
    s2 = s2+s1[-i]
    i += 1
if(s2 == s1):
    print("palindrome")
else:
    print("not a palindrome")
rno = int(s2)
print(rno)
