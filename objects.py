import random


class Character():
    def __init__(self,name,health,order):
        self.name = name
        self.health = health
        self.order = order

class Dice():
    def __init__(self,sides):
        self.sides = sides
        self.name = ("d"+str(sides))
    def roll(self):
        value = 0
        value = random.randint(1,self.sides)

        return value