# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:36:32 2024

@author: Shohruh
"""

lst=[[1, 'Jean Castro', 'V'],
[2, 'Lula Powell', 'V'],
[3, 'Brian Howell', 'VI'],
[4, 'Lynne Foster', 'VI'],
[5, 'Zachary Simon', 'VII']]

dict1={}
for i in lst:
    try:
        dict1[i[0]]=i[1:]

    except Exception as e:
        print(e)
        
        
print(dict1)
