# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 22:30:53 2024

@author: Shohruh
"""
set1={4,5,6,7,8,9} 
set2={5,6,7,10,11}
set3=set1.symmetric_difference(set2)
set4=set1.intersection(set2)
print(sum(set3)-sum(set4))