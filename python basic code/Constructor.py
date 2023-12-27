class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"Hi Iam {self.name}")


person1 = Person("John")
person1.talk()

person2 = Person("Bob")
person2.talk()
