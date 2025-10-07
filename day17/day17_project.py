class User:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"Hi, my name is {self.name}"


user1 = User('John')
user2 = User('Amari')


print(user1)

print(user2)
