# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 22:56:22 2024

@author: Shohruh
"""

def func(list1,list2):
    list3=[]
    max1=max(len(list1),len(list2))
    
    for i in range(max1):
        if i<len(list1):
            list3.append(list1[i])  
        if i<len(list2):
            list3.append(list2[i])  
    return list3
print(func([1, 2, 3], [11, 22, 33]))           
print(func([1, 2, 3, 4, 5], [11, 22, 33]))     
print(func([1, 2], [11, 22, 33, 44, 55]))      

