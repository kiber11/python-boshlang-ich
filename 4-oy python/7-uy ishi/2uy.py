# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 21:22:25 2024

@author: Shohruh
"""

soz=input("so'z kiriting: ")

with open('2matn.txt', 'r',encoding='utf-8') as fayl:
    a=fayl.read()


index=a.find(soz)

if index != -1:
    print(f"'{soz}' so'zi faylda topildi, {index}-pozitsiyada.")
else:
    print(f"'{soz}' so'zi faylda topilmadi.")
