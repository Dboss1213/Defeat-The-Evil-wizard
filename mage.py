
from character import Character


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def special_ability(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} casts Fireball on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} has been defeated!")
