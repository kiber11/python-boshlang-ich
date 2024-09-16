# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 20:50:33 2024

@author: Shohruh
"""
# with open('1input.txt','r') as f:
#     lst = f.read().split()

# result=''.join(chr(int(i)) for i in  lst)


# with open('1output.txt', 'w') as f:
#    f.write(result)



f=open('1input.txt','r')
lst=f.read().split()
f.close()

result= ''
for i in lst:
    result +=chr(int(i))

f = open('1output.txt', 'w')
f.write(result)
f.close()


