class User:
    user_count = 0
    usernames = set()

    def __init__(self, username, password, age):
        if username in User.usernames:
            raise ValueError(f"{username} allaqachon ishlatilgan!")
        self.username = username
        self.password = password
        self.age = age
        
        User.usernames.add(username)
        User.user_count += 1
    
    @classmethod
    def get_user_count(cls):
        return cls.user_count

try:
    user1 = User("ali123", "password1", 25)
    print(f"Foydalanuvchi yaratildi: {user1.username}")
    
    user2 = User("vali456", "password2", 30)
    print(f"Foydalanuvchi yaratildi: {user2.username}")

    user3 = User("ali123", "password3", 20) 
except ValueError as e:
    print(e)

print(f"Jami foydalanuvchilar soni: {User.get_user_count()}")
