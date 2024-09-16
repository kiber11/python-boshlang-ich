# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 22:01:26 2024

@author: Shohruh
"""

with open('3in.txt', 'r', encoding='utf-8') as f:
    matn=f.readlines()

yangi_matn=[]
for qator in matn:
    yangi_qator=qator.title() 
    yangi_matn.append(yangi_qator)

with open('3in.txt','w',encoding='utf-8') as f:
    f.writelines(yangi_matn)


