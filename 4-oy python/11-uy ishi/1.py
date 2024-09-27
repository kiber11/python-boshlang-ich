
class Talaba:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print(f"Name: {self.name} \nAge: {self.age}")

class Kurs:
    def __init__(self, kurs_name, kurs_teacher):
        self.kurs_name = kurs_name
        self.kurs_teacher = kurs_teacher
        self.talabalar = []  
        self.talabalar_soni = 0  

    def add(self, talaba):
        if self.talabalar_soni < 10:  
            self.talabalar.append(talaba)
            self.talabalar_soni += 1
            print(f"{talaba.name} {self.kurs_name} kursiga qo'shildi.")
        else:
            print(f"Xatolik: {self.kurs_name} kursida maksimal 10 talaba mavjud!")

    def delete_talaba(self, talaba):
        if talaba in self.talabalar:
            self.talabalar.remove(talaba)
            self.talabalar_soni -= 1
            print(f"{talaba.name} {self.kurs_name} kursidan o'chirildi.")

    def get_info(self):
        print(f"Kurs nomi: {self.kurs_name}")
        print(f"O'qituvchi: {self.kurs_teacher}")
        print(f"Talabalar soni: {self.talabalar_soni}")
        print(f"{self.kurs_name} kursidagi talabalar:")
        for talaba in self.talabalar:
            talaba.get_info()
        print("-" * 30)

talaba1 = Talaba("Shohruh", 21)
talaba2 = Talaba("Azizbek", 22)
talaba3 = Talaba("Nurlan", 23)
talaba4 = Talaba("Abdulloh", 24)
talaba5 = Talaba("Umid", 25)
talaba6 = Talaba("Doston", 20)
talaba7 = Talaba("Javohir", 19)
talaba8 = Talaba("Sabina", 22)
talaba9 = Talaba("Aygul", 23)
talaba10 = Talaba("Farhod", 26)
talaba11 = Talaba("Sardor", 28)  

python_kurs = Kurs("Python", "Avaz")
java_kurs = Kurs("Java", "Qurbonali")

for talaba in [talaba1, talaba2, talaba3, talaba4, talaba5, talaba6, talaba7, talaba8, talaba9, talaba10]:
    python_kurs.add(talaba)

python_kurs.add(talaba11)  

for talaba in [talaba1, talaba2, talaba3, talaba4, talaba5, talaba6, talaba7, talaba8, talaba9, talaba10]:
    java_kurs.add(talaba)

java_kurs.add(talaba11)  

python_kurs.get_info()
java_kurs.get_info()
python_kurs.delete_talaba(talaba1)
java_kurs.delete_talaba(talaba3)
python_kurs.get_info()
java_kurs.get_info()

# class Talaba:
#     python={}
#     java={}
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def get_info(self):
#         print(f"Name:{self.name} \nAge:{self.age}")

# class Kurs(Talaba):
#     talabalar_soni_py = 0
#     talabalar_soni_jv = 0
#     talabalar=[]
#     def __init__(self,name,age,kurs_name,kurs_teacher):
#         super().__init__(name,age)
#         self.kurs_name = kurs_name
#         self.kurs_teacher = kurs_teacher
#         if self.kurs_name == "Python":
#             Kurs.talabalar_soni_py+=1
#         else:
#             Kurs.talabalar_soni_jv+=1
#         self.talabalar_soni = Kurs.talabalar_soni_py + Kurs.talabalar_soni_jv
#     def __add__(self,name,age,kurs_name):
#         if self.kurs_name=="Python":
#             Talaba.python[name]=age
#             self.talabalar_soni+=1
#             Kurs.talabalar_soni_py+=1
#             Kurs.talabalar.append(Talaba.python)
#         else:    
#             Talaba.java[name]=age
#             self.talabalar_soni+=1
#             Kurs.talabalar.append(Talaba.java)
#             Kurs.talabalar_soni_jv+=1
#     def delete_talaba(self,name,kurs_name):
#         if kurs_name=="Python":
#             self.talabalar.remove(Talaba.python[name])
#             self.talabalar_soni-=1
#         else:
#             self.talabalar.remove(Talaba.java[name])
#             self.talabalar_soni-=1
#     def get_info(self):
#         for talaba in self.talabalar:
#             print(f"{talaba.name},yoshi:{talaba.age}")
#             print(f"Talabalar soni:{self.talabalar_soni} \nKurs nomi:{self.kurs_name} \nO'qituvchi:{self.kurs_teacher}_")
#         print("-"*30)

# talaba1=Kurs("Shohruh",21,"Python","Avaz")
# talaba2=Kurs("Azizbek",22,"Python","Avaz")
# talaba3= Kurs("Nurlan",23,"Java","Qurbonali")
# talaba4=Kurs("Abdulloh",24,"Java","Qurbonali")
# talaba1.get_info()
# talaba2.get_info()
# talaba3.get_info()

# class Talaba:
#     python = {}
#     java = {}

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_info(self):
#         print(f"Name: {self.name} \nAge: {self.age}")

# class Kurs:
#     talabalar_soni = 0

#     def __init__(self, kurs_name, kurs_teacher):
#         self.kurs_name = kurs_name
#         self.kurs_teacher = kurs_teacher
#         self.talabalar = []

#     def add(self, talaba):
#         if self.kurs_name == "Python":
#             Talaba.python[talaba.name] = talaba.age
#         else:
#             Talaba.java[talaba.name] = talaba.age
#         self.talabalar.append(talaba)
#         Kurs.talabalar_soni += 1

#     def delete_talaba(self, talaba):
#         if self.kurs_name == "Python":
#             Talaba.python.pop(talaba.name, None)
#         else:
#             Talaba.java.pop(talaba.name, None)
#         self.talabalar.remove(talaba)
#         Kurs.talabalar_soni -= 1

#     def get_info(self):
#         print(f"Kurs name: {self.kurs_name}\nKurs teacher: {self.kurs_teacher}\nTalabalar soni: {len(self.talabalar)}")
#         print("Talabalar ro'yxati:")
#         for talaba in self.talabalar:
#             print(f"- {talaba.name}, Yoshi: {talaba.age}")
#         print("-" * 30)


# talaba1 = Talaba("Shohruh", 21)
# talaba2 = Talaba("Azizbek", 22)
# talaba3 = Talaba("Nurlan", 23)
# talaba4 = Talaba("Abdulloh", 24)


# python_kurs = Kurs("Python", "Bahodir")
# java_kurs = Kurs("Java", "Qurbonali")


# python_kurs.add(talaba1)
# python_kurs.add(talaba2)
# java_kurs.add(talaba3)
# java_kurs.add(talaba4)


# python_kurs.get_info()
# java_kurs.get_info()


# python_kurs.delete_talaba(talaba1)
# java_kurs.delete_talaba(talaba3)

# python_kurs.get_info()
# java_kurs.get_info()


# class Talaba:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # Kurs klassi
# class Kurs:
#     def __init__(self, kurs_name, kurs_teacher):
#         self.kurs_name = kurs_name
#         self.kurs_teacher = kurs_teacher
#         self.talabalar_soni = 0
#         self.talabalar = []

#     # Talaba qo'shish metodi
#     def add(self, new_student):
#         self.talabalar.append(new_student)
#         self.talabalar_soni += 1

#     # Talabani kursdan o'chirish metodi
#     def delete(self, new_student):
#         self.talabalar = [talaba for talaba in self.talabalar if talaba.name != new_student.name]
#         self.talabalar_soni -= 1

#     # Kurs haqida ma'lumot chiqarish metodi
#     def info_kurs(self):
#         print(f"Kurs nomi: {self.kurs_name}")
#         print(f"O'qituvchi: {self.kurs_teacher}")
#         print(f"Talabalar soni: {self.talabalar_soni}")
#         print("Talabalar ro'yxati:")
#         for talaba in self.talabalar:
#             print(f"{talaba.name}, Yoshi: {talaba.age}")
#         print("-" * 30)

# # 10 ta talaba yaratamiz
# talabalar = [Talaba(f"Talaba{i+1}", 20+i) for i in range(10)]

# # 2 ta kurs e'lon qilamiz
# kurs1 = Kurs("Python", "Bahodir")
# kurs2 = Kurs("Java", "Otabek")

# # Har bir kursga 10 tadan talaba qo'shamiz
# for talaba in talabalar:
#     kurs1.add(talaba)
#     kurs2.add(talaba)

# # Kurslar haqida ma'lumot chiqaramiz
# kurs1.info_kurs()
# kurs2.info_kurs()

# # 2 ta talabani kursdan chiqaramiz
# kurs1.delete(talabalar[0])  # Talaba1 ni kurs1dan chiqaramiz
# kurs2.delete(talabalar[1])  # Talaba2 ni kurs2dan chiqaramiz

# # Kurslar haqida ma'lumotni qayta chiqaramiz
# kurs1.info_kurs()
# kurs2.info_kurs()
