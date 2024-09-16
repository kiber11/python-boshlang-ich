# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:20:41 2024

@author: Shohruh
"""

import random
import math
a=[]
for i in range(10):
    a.append(random.randint(1, 40))
with open('6sonlar.txt',"w") as f:
    for i in a:
        f.write(str(i)+'\n')
b=[]
with open('6sonlar.txt','r') as f:    
    for i in f:
        b.append(int(i.strip()))
c=sum(b)/len(b)

if math.ceil(c)-c>0.5:
    print(f'o\'rtachasi={c}\nyaxlit={math.floor(c)}')
else:
    print(f'o\'rtachasi={c}\nyaxlit={math.ceil(c)}')

