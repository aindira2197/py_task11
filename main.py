class Animal:
    def sound(self):
        print("Hayvon ovoz chiqarmoqda")

class Dog(Animal):
    def sound(self):
        print("Vov-vov")

dog = Dog()
dog.sound()
