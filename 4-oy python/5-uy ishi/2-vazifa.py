# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 22:17:02 2024

@author: Shohruh
"""

def func(a):
    i=0
    while i<len(a):
        if a.count(a[i])>1:
            a.pop(i)
        else:    
            i+=1
    return a
a= [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

print(func(a))

#2-usul
a = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

# Har bir ichki ro'yxatni tuple ga o'zgartirish va set ga aylantirish
a = set(tuple(sublist) for sublist in a)

# Natijani ro'yxatga qaytarish
a = list(a)

print(a)


