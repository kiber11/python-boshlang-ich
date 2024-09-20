


class Employee:
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age
        self._family=["Shohruh","Shohruh1","Shohruh2"]
        self.__salary=20000
    def change_salary(self):
        maosh=int(input("Maoshni kiriting: "))
        self.__salary=maosh
        return f'O\'zgargan maosh: {self.__salary}' 
    def __str__(self):
        return f"ismi:{self.name}\nFamiliyasi:{self.surname}\nYoshi:{self.age}\nOilasi:{self._family}\nMaoshi: {self.__salary}"
a=Employee("Shohruh","Abdullayev",25)
print(a.__str__())
print(a.change_salary())    