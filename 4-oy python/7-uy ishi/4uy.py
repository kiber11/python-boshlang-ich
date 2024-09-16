# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 22:08:25 2024

@author: Shohruh
"""

#1-usul
with open('4ismlar1.txt', 'r',encoding='utf-8') as f:
    ismlar=f.readlines()
print(ismlar)

ismlar1=[]
for ism in ismlar:
    ism_tozalangan = ism.strip().capitalize()  
    if ism_tozalangan not in ismlar1:
        ismlar1.append(ism_tozalangan)


with open('4ismlar.txt', 'w', encoding='utf-8') as f:
    for ism in ismlar1:
        f.write(ism + '\n')

#2-usul
with open('4ismlar1.txt', 'r', encoding='utf-8') as f:
    ismlar = f.read() 


ismlar = ismlar.replace('\n', ' ')  
ismlar = ismlar.split() 

ismlar1 = []
for ism in ismlar:
    ism_tozalangan = ism.strip(",.;").capitalize()  
    if ism_tozalangan not in ismlar1:
        ismlar1.append(ism_tozalangan)


with open('4ismlar.txt', 'w', encoding='utf-8') as f:
    for ism in ismlar1:
        f.write(ism + '\n')


