import random


class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def __str__(self):
        return f"{self.name}: {self.hp}HP"

    def on_attack(self):
        if random.randint(1, 2) == 1:
            print("Your attack was successful")
            self.hp -= 1
        else:
            print("Your attacked missed!")
