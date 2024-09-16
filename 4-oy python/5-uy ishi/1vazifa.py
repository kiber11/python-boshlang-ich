# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 20:02:37 2024

@author: Shohruh
"""


a= [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9 , 7, 1]
print(len(a))
def func(a):
    soni=a.count(0)  
    i=0
    while i<len(a):
        if a[i]==0:
            a.pop(i)  
        else:
            i+=1  
    a.extend([0]*soni)  
    print(a)

func(a)
        