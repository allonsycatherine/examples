# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:28:56 2022

@author: Катя
"""
class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def perimeter (self):
        per = 2 * (self.length + self.width)
        print (per)
        return per
    def area (self):
        ar = self.length * self.width
        print (ar)
        return ar

first = Rectangle(12, 5)
per1 = first.perimeter()
ar1 = first.area()

second = Rectangle(1, 5)
ar2 = second.area()

class Square (Rectangle):
    def __init__(self, length, width):
        self.length = length
        self.width = width
square1 = Square (15, 15)
per4 = square1.perimeter()

