# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:34:00 2024

@author: Shohruh
"""
import random
lst=[]
son=0   

for i in range(10):
        
    num=random.randint(1, 100)
    if num%2==0:
        son+=1
    lst.append(num)

print(son)
print(lst)
    
