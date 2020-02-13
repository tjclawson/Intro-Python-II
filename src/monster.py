class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def __str__(self):
        return f"{self.name}: {self.hp}HP"

    def on_attack(self):
        self.hp -= 1
