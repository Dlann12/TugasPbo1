class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} makes {self.sound} sound")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "meow")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "bark")


my_cat = Cat("Fluffy")
my_dog = Dog("Buddy")

my_cat.make_sound()  # Output: Fluffy makes meow sound
my_dog.make_sound()  # Output: Buddy makes bark sound