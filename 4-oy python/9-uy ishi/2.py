class restoran:
    def __init__(self,vaqti):
        self.vaqti = vaqti
        self.menyusi = {}

    def menyu_ochish(self, nom, narx):
        while True:
            try:
                nom=input("Menyuga yangi ovqat qo'shish(Dasturdan chiqish uchun 1 ni bosing): ")
                if nom == "1":
                    break
                narx=int(input("Narxini kiriting: "))
                if nom not in self.menyusi:
                    self.menyusi[nom]=narx
                else:
                    print("Bu ovqat menyuda bor")
            except ValueError:
                print("narxini to'g'ri kiriting!!!")
        
    def info(self):
        for i,j in self.menyusi.items(): #menyusi
            print(f'nomi:{i}\nnarxi:{j}\n')  
a=restoran("10:00 dan 21:00 gacha")
print(f'ish vaqti:{a.vaqti}')
a.menyu_ochish("osh",20000)
a.info()
