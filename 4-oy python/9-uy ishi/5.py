class Employee:
    def __init__(self,ismi,familiyasi,ish_joy_sana,lavozimi,maoshi,bonus):
        self.ismi=ismi
        self.familiyasi=familiyasi
        self.ish_joy_sana=ish_joy_sana
        self.lavozimi=lavozimi
        self.maoshi=maoshi
        self.bonus=bonus
    def maosh(self):
        if self.maoshi<10000000:
            self.bonus=self.maoshi/4
        print(f"Maosh: {self.maoshi}, Bonus: {self.bonus}")

a=Employee("Shohruh","Abdullayev","01.01.2022","Dasturchi",8000000,0)
a.maosh()