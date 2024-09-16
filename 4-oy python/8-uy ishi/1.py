lst = ["A","B","C","D","E","F","G","L","Q","U"]
a=int(input('Son kiriting: '))
natija = []
i = 0
while i<len(lst):
    natija.append(lst[i:i+a])
    i+=a

print(natija)
