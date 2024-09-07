# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:24:57 2024

@author: Shohruh
"""
#1-usul:
a=int(input('a='))
b=int(input('b='))
c=list(range(a,b))
print(str(c[3])+','+str(c[-4]))
 
#2-usul:
if len(c)>3:
     print(c[3],end=',')
if len(c)>=4:
     print(c[-4])
    