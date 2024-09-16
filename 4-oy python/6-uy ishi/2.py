# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 20:59:54 2024

@author: Shohruh
"""

lst=["Salom", "123", "56", "Python", "Try", "90", "Except"]
lst2=[]

# for i in lst:
#     try:
#         num=int(i)
#         lst2.append(int(i))
#     except ValueError:
#         continue
# print(lst2)

#2-usul:
for j in lst:
    try:
        if j.isdigit():
            lst2.append(int(j))
    except Exception as e:
        print(e)

print(lst2)
        
    
    