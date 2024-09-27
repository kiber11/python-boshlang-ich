class Taqvim:

    def __init__(self, hijriy,grigoriy):
        self.hijriy=hijriy
        self.grigoriy=grigoriy
    def hijriy_date(self):
         return (self.grigoriy - 622)*33//32

    def grigoriy_date(self):
        return self.hijriy*32//33+622

a=Taqvim(1445,2024)
print(a.hijriy_date())
print(a.grigoriy_date())
