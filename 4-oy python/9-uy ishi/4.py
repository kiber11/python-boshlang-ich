class phone :
    def __init__(self,brand,model,narx,yili):
        self.brand = brand
        self.model = model
        self.narx = narx
        self.yili = yili
    def update_price(self,narx):
        price=int(input("Narxni kiriting:"))
        self.narx = price
        print(f'narxi:{self.narx}')
    def info(self):
        print(f"Brand:{self.brand}\nModel:{self.model}\nNarxi:{self.narx}\nYili:{self.yili}")
a=phone("samsung","note10",20000,2020)
a.update_price(30000)
a.info()
    