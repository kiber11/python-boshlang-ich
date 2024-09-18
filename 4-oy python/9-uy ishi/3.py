
class foydalanuvchi:
    def __init__(self,name,username,followers):
        self.name=name
        self.username=username
        self.followers=followers
        self.following=[]
    def follow(self,user):
        while True:
            print('Taklif qilishni to\'xtatish uchun 1 ni bosing')
            user=input("Foydalanuvchi nomini kiriting: ")
            if user == "1":
                break
            if user in self.following:
                print("Foydalanuvchi allaqachon taklif qilgan")
            else:
                self.following.append(user)
    def unfollow(self,user):
        while True:
            print('o\'chirishni to\'xtatish uchun 1 ni bosing')
            user=input("Foydalanuvchi nomini kiriting: ")
            if user=='1':
                break
            if user in self.following:
                self.following.remove(user)
            else:
                print("Bunday foydalanuvchi ro'yxatda yo'q")
    def remove_follower(self,user):
        while True:
            print('Followerlarni o\'chirishni to\'xtatish uchun 1 ni bosing')
            user=input("Foydalanuvchi nomini kiriting: ")
            if user=='1':
                break
            if user in self.followers:
                self.followers.remove(user)
            else:
                print("Bunday foydalanuvchi ro'yxatda yo'q")
    def info(self):
        print(f"Foydalanuvchi nomi:{self.name}\n"
            f"Foydalanuvchi usernami:{self.username}\n")
        print('Obunalar ro\'yxati:')
        if len(self.following)==0:
            print("Obunalar ro'yxati bo'sh")
        else:    
            for i in self.following:
            
                print(i)
        print('Followerlarni ro\'yxati:')
        for i in self.followers:
            print(i)
a=foydalanuvchi('Shohruh','shohruh',['Shohruh','Shohruh1','Shohruh2'])
a.follow('Shohruh1')    
a.unfollow('Shohruh')
a.remove_follower('Shohruh1')
a.info()
