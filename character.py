###### Defeat the evil wizard ######

class Character: 
    def __init__(self, name, health, attack_power): 
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        healed_amount = 25
        self.health = min(self.health + healed_amount, self.max_health)
        print(f"{self.name} heals for {healed_amount}! Current health: {self.health}/{self.max_health}")

    def display_stats(self):
        print(f"\n{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

