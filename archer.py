
from character import Character

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)

    def special_ability(self, opponent):
        damage = self.attack_power + 10
        opponent.health -= damage
        print(f"{self.name} uses Piercing Arrow on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} has been defeated!")