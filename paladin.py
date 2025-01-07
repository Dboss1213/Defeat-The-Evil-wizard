
from character import Character


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)

    def special_ability(self):
        healed_amount = 40
        self.health = min(self.health + healed_amount, self.max_health)
        print(f"{self.name} uses Divine Light and heals for {healed_amount}! Current health: {self.health}/{self.max_health}")
