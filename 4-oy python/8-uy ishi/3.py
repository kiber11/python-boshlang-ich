a=input('so\'z kiriting: ')
dict1={}
def fun(a):
    
    for i in a:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    return dict1
print(fun(a))