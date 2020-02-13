from monster import Monster
from player import Player


class Battle:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def battle(self):
        while self.monster.hp != 0:
            print("\nTHERE IS A MONSTER IN THIS ROOM!")
            print(self.monster)
            option = input('What will you do? Use "attack" to attack the monster, use "run" to run away: ')
            if option == "run":
                self.player.current_room = self.player.last_room
                break
            elif option == "attack":
                if self.player.has_weapon():
                    self.monster.on_attack()
                    if self.monster.hp == 0:
                        self.player.current_room.monster = None
                        print("You defeated the monster!")
                else:
                    print("You do not have a weapon to attack with!")
            else:
                print("Please enter a valid command")
        return self.player

