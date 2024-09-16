# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 23:13:08 2024

@author: Shohruh
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def func(x):
    return x in b
new=list(filter(func,set(a)))

print(new)
    