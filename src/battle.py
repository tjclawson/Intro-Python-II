from monster import Monster
from player import Player


class Battle:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def print_monster_presence(self):
        if self.player.current_room.is_room_illuminated:
            print("\nTHERE IS A MONSTER IN THIS ROOM!")
            print(self.monster)
        else:
            print("\nYOU CAN HEAR A MONSTER IN THIS ROOM!")

    def battle(self):
        while self.monster.hp != 0:
            self.print_monster_presence()
            print(f"{self.player.name}: {self.player.hp}HP")
            option = input('What will you do? Use "attack" to attack the monster, use "run" to run away: ')
            if option == "run":
                self.player.current_room = self.player.last_room
                break
            elif option == "attack":
                if self.player.has_weapon() and self.player.current_room.is_room_illuminated:
                    self.monster.on_attack()
                    if self.monster.hp == 0:
                        self.player.current_room.monster = None
                        print("You defeated the monster!")
                        break
                    print(f"{self.monster.name} is attacking!")
                    self.player.on_attack()
                    if self.player.hp == 0:
                        for i in range(1, 10):
                            print("GAME OVER")
                        break
                elif self.player.has_weapon() and not self.player.current_room.is_room_illuminated:
                    print("You cannot attack the monster because you cannot see!")
                else:
                    print("You do not have a weapon to attack with!")
            else:
                print("Please enter a valid command")
        return self.player

