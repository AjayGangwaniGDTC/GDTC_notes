class Animal():
    def sound(self):
        print('Some generic animal sound')

class Dog(Animal):
    def sound(self):
        print('Dog Barks')

class Cat(Animal):
    def sound(self):
        print('Cat Meows')

for animal in [Dog(), Cat()]:
    animal.sound()