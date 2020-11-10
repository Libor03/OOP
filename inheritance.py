class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 20

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


mammal = Mammal()
print(mammal.__dict__)
print(isinstance(mammal, Animal))
print(issubclass(Mammal, object))

fish = Fish()
fish.swim()
fish.eat()
