class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    def bark(self):
       print("bark")
class Cat(Mammal):
    def eat(self):
        print("eat")

dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.eat()
