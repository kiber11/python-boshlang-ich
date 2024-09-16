
for i in range(10,100):
  
    tub=1
    for l in range(2,i):
        if i%l!=0:
            tub=1
        
        else:
            tub=0
            break
    if tub==1:
        print(i,end=' ')
    


       
           