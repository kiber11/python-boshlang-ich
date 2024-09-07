# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 22:19:00 2024

@author: Shohruh
"""

set1={'olma', 'anor', 'youtube', 'instagram', 'gilos'}
set2={'youtube', 'gilos', 'anor', 'BMW', 'Tesla', 'Nissan'}
set3={'gilos', 'olma', 'instagram', 'Tesla', 'Nissan'}

set4=set1.intersection(set2)
set4.difference_update(set3)
