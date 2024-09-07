son=int(input('son kiriting: ')) 
son2=0
while son!=0:
    son2=son2*10+son%10
    son=son//10
print(son2)