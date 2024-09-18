class avto:
    def __init__(self, name,rangi, narxi,probeg,tezlik ):
        self.name = name
        self.rangi = rangi
        self.narxi = narxi
        self.probeg = probeg
        self.tezlik = tezlik
    def update_probeg(self,probeg):
        prob=input("probegni kiriting:")
        self.probeg = prob
    def update_narxi(self,narxi):
        narx=int(input("narxni kiriting:"))
        self.narxi = narxi

a=avto("audi","qora",10000,100,1000)
print(f'Nomi:{a.name}\nRangi:{a.rangi}\nNarxi: {a.narxi}\nProbegi:{a.probeg}\nTezlik:{a.tezlik}')
a.update_narxi(20000)

a.update_probeg(200)
print(a.probeg,a.narxi)