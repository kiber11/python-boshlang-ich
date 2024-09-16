# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:41:05 2024

@author: Shohruh
"""

a= [(10,20,40),(40,50,60),(70,80,90)]
b=[]
for i in a:
    c=list(i)
    c[-1]=100
    b.append(tuple(c))
print(b)