from abc import ABC,abstractmethod
class Player(ABC):
    @abstractmethod
    def kick(self):
        pass
    @abstractmethod
    def run(self):
        pass
    @abstractmethod
    def jump(self):
        pass
    @abstractmethod
    def shoot(self):
        pass
class MasterChief(Player):
    def __init__(self,user):
        self.user = user

    def kick(self):
        print("kick")
    def run(self):
        print("run")
    def jump(self):
        print("jump")
    def shoot(self):
        print("shoot")

    def __str__(self):
        return f"{self.user}"

user = MasterChief("Olim123")

print(user)
user.kick()
user.run()
user.jump()
user.shoot()