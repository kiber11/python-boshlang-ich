lst=[]
temp=0
ishora=True
for i in range(6):
    a=int(input(f'{i+1}-sonni kiriting: '))
    lst.append(a)
    if a<temp:
        ishora=False
    temp=a
if ishora:
    print('Tartiblangan')
else:
    print('Tartiblanmagan')
