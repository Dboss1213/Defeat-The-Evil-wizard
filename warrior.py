from character import Character

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def special_ability(self, opponent):
        damage = self.attack_power * 1.5
        opponent.health -= damage
        print(f"{self.name} uses Power Strike on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} has been defeated!")

