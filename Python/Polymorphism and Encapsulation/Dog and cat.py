class Cat:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def speak(self):
        print(f"I am a cat. .My name is {self.name}. I am {self.age}years old")

    def makesound(self):
        print("Meow")    

class Dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def speak(self):
        print(f"I am a Dog. .My name is {self.name}. I am {self.age}years old")

    def makesound(self):
        print("Bark")

cat1 =Cat("Ginger",2 )
dog1 =Dog("Bruno",4 )

for animal in (cat1,dog1):
    animal.makesound()
    animal.speak()