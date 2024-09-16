# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:24:28 2024

@author: Shohruh
"""
import math
lst=[16, "Pip", False, {}, 25, 49, 144,True, "Modul"]
for i in lst:
    try:
        if i==False or i==True:
            continue
        num=int(i)
        print(f'{i}->{int(math.sqrt(i))}')
    except :
        continue
        

