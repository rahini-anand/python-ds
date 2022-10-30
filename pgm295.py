#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no :295
Created on Fri Oct 14 12:35:30 2022
Title: define shape class
@author: rahini
"""
from abc import ABC, abstractmethod


class shape(ABC):
    @abstractmethod
    def draw():
        pass

    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimeter():
        pass
