class Animal:
    def __init__(type, name, sound):
       type.name = name
       type.sound = sound

    def make_sound(type):
        print(f"{type.name} makes {type.sound} sound")


class Cat(Animal):
    def __init__(type, name):
        super().__init__(name, "meow")


class Dog(Animal):
    def __init__(type, name):
        super().__init__(name, "bark")


my_cat = Cat("Fluffy")
my_dog = Dog("Buddy")
# melakukan pemanggilan output setelah  membuat method method diatas 
my_cat.make_sound()  # Output: Fluffy makes meow sound
my_dog.make_sound()  # Output: Buddy makes bark sound
