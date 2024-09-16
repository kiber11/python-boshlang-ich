# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 21:29:21 2024

@author: Shohruh
"""

N1=int(input('1-setning indekslar sonini kiriting:'))
N2=int(input('2-setning indekslar sonini kiriting:'))
a=set()
b=set()
for i in range(1,N1+1):
    if i==N1:
        a.add(int(input(f"1-setning oxirgi elementi:")))
    else:
        a.add(int(input(f"1-setning {i}-elementi:")))
    
for i in range(1,N2+1):
    if i==N2:
        b.add(int(input('2-setning oxirgi elementi:')))
    else:
        b.add(int(input(f"2-setning {i}-elementi:")))
set4=a.intersection(b)
set5=a.difference(b)

print('oxirgi natija:',sum(set4)-sum(set5))





                    
