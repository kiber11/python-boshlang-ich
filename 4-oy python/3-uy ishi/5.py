# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:10:56 2024

@author: Shohruh
"""
a=[]
b=[]
c=[]
for i in range(4):
    a = [0] * 3
    
    for k in range(3):
        a[k]=int(input(f"{i+1} ro'yxat va {k+1} elementi: "))
    b.append(list(a))
    c.append(sum(b[i]))
print(max(b))