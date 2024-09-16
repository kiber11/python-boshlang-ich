# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 20:44:18 2024

@author: Shohruh
"""

a=input('qiymat kiriting: ')
b={}

for i in range(len(a)):
    b.update({a[i]:a.count(a[i])}) # yoki b[a[i]]=a.count(a[i])
print(b)
