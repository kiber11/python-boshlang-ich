3# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 23:23:19 2024

@author: Shohruh
"""

N=int(input('list elementi soni:'))
a=[]
def func(a):
    for i in range(N):
        a.append(input(f'{i+1}-elementni kiriting:'))
    print('dastlabki:',a)
    j=0
    while j<len(a):
        if a.count(a[j])==1:
            a.pop(j)
        else:
            j+=1
    return a
print(func(a))