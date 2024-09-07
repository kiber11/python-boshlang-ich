# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 21:23:46 2024

@author: Shohruh
"""

N=int(input('son kiriting>>>'))
dik1={}
for i in range(1,N):
    dik1.update({i:i**2})
print(dik1)