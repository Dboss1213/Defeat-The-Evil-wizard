from character import Character

class Evil_Wizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        healed_amount = 10
        self.health = min(self.health + healed_amount, self.max_health)
        print(f"{self.name} regenerates {healed_amount} health! Current health: {self.health}/{self.max_health}")
