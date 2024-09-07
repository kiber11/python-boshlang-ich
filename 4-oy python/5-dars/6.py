# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 22:36:50 2024

@author: Shohruh
"""

a=int(input('Qancha mahsulot sotasiz?:'))
bozor={}
for i in range(a):
    mahsulot_nomi=input('mahsulot nomi:')
    narxi=int(input('narxi:'))
    bozor[mahsulot_nomi]=narxi
print(bozor)
#2-usul:
mahsulotlar = {}

while True:
    mahsulot = input("Mahsulot nomi (yoki 'stop' uchun yozing): ").lower()
    if mahsulot == 'stop':
        break
    narx = input(f"{mahsulot.capitalize()} narxi: ")
    mahsulotlar[mahsulot] = narx

print("\nMahsulotlar va ularning narxlari:")
for mahsulot, narx in mahsulotlar.items():
    print(f"{mahsulot.capitalize()}: {narx} so'm")
