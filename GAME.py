from warrior import Warrior
from mage import Mage
from archer import Archer
from paladin import Paladin
from EvilWizard import Evil_Wizard



def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your hero class: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
  
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        print("5. Quit")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Paladin):
                player.special_ability()
            else:
                player.special_ability(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        elif choice == '5':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice, try again.")
            continue

        if wizard.health > 0:
            print("\n--- Wizard's Turn ---")
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The evil wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = Evil_Wizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
    