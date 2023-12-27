import random

class Dice:
    def roll(self):
        first=random.randint(3,6)
        second = random.randint(3,6)
        return first,second
dice = Dice()
print(dice.roll())





















for i in range(3):
    print(random.randint(10,20))


memebers = ['John','Alice','Bob','Mosh']
leader = random.choice(memebers)
print(leader)

