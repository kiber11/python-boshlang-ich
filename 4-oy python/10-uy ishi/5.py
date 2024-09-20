from pyexpat import model


class Texnika:
    def __init__(self,brand,model,narx):
        self.brand = brand
        self.model = model
        self.narx = narx
    def xususiyat(self):
        pass
    def __str__(self):
        return f"{self.brand} {self.model} {self.narx}"

class smartfon(Texnika):
    def __init__(self,brand,model,narx,CPU,operativka,ekran,xotira):
        self.CPU=CPU
        self.operativka=operativka
        self.ekran=ekran
        self.xotira=xotira
        super().__init__(brand,model,narx)
    def __str__(self):
        return f"Brand:{self.brand}\nModel:{self.model}\nNarxi:{self.narx}\nCPU:{self.CPU}\nOperativka:{self.operativka}\nEkran:{self.ekran}\nXotira:{self.xotira}\n"
class Noutbook(Texnika):
    def __init__(self,brand,model,narx,CPU,GPU,operativka,ekran,xotira,):
        self.operativka=operativka
        self.ekran=ekran
        self.xotira=xotira
        self.GPU=GPU
        self.CPU=CPU
        super().__init__(brand,model,narx)
    def __str__(self):
        texnika_str=super().__str__()
        return f"{texnika_str}\nCPU:{self.CPU}\nGPU:{self.GPU}\nOperativka:{self.operativka}\nEkran:{self.ekran}\nXotira:{self.xotira}\n"
class Mashina(Texnika):
    def __init__(self,brand,model,narx,rangi,ot_kuchi,yili):
        self.rangi=rangi
        self.ot_kuchi=ot_kuchi
        self.yili=yili
        super().__init__(brand,model,narx)
    def __str__(self):
        texnika_str=super().__str__()
        return f"{texnika_str}\nRangi:{self.rangi}\nOt kuchi:{self.ot_kuchi}\nYili:{self.yili}"
a=smartfon("apple","iphone 16","1000000","bionic 18","16gb","IPS","128gb")
b=Noutbook("apple","macbook","1000000","M1 pro","Nvidia GTX","16GB","IPS","1TB")
c=Mashina("BMW","X5","1000000","qora","ot kuchi","2020")
print(a)
print(b)
print(c)
