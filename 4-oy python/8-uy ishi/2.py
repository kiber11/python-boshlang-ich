myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
mydict={}
def function(myList):
    for i in myList:
        if i in mydict:
            mydict[i]+=1
        else:
            mydict[i]=1
    return mydict
print(function(myList))