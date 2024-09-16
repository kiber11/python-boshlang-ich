# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:45:17 2024

@author: Shohruh
"""
from googletrans import Translator
lst=["salom", 12, "dastur", True, "yordam", "kitob", 3.14]
dict1={}
tarjimon=Translator()
for i in range(len(lst)):
    
    if type(lst[i])==str:
        res=tarjimon.translate(lst[i],src='uz',dest='en')
        dict1[lst[i]]=res.text
    else:
        continue
print(dict1)

