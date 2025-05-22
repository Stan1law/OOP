# Activity 2: RPG Character Simulator
# Instructions:
# Create a character simulation program using full OOP principles. The system must allow users to create a game character, display its details, and allow leveling up based on user interaction. All data should be encapsulated and accessed only through methods.
# Expected Output:
# Enter character name: QuantumSaga
# Enter class type (warrior/mage/archer): warrior
# Enter initial level: 1

# Character created!
# Name: QuantumSaga
# Class: warrior
# Level: 1

# Do you want to level up? (yes/no): yes
# Congratulations! QuantumSaga has leveled up to 2

# Updated Character info:
# Name: QuantumSaga
# Class: warrior
# Level: 2

class Character:
    def __init__(self, name, class_type, level):
        self.__name = name
        self.__class_type = class_type
        self.__level = level

    def get_name(self):
        return self.__name

    def get_class_type(self):
        return self.__class_type

    def get_level(self):
        return self.__level

    def level_up(self):
        self.__level += 1
        print(f"Congratulations! {self.__name} has leveled up to {self.__level}")

    def display_info(self):
        print("\nCharacter info:")
        print(f"Name: {self.__name}")
        print(f"Class: {self.__class_type}")
        print(f"Level: {self.__level}")

if __name__ == "__main__":
    valid_classes = ["warrior", "mage", "archer"]
    name = input("Enter character name: ")

    while True:
        class_type = input("Enter class type (warrior/mage/archer): ").lower()
        if class_type in valid_classes:
            break
        print("Invalid class type! Please enter warrior, mage, or archer.")

    while True:
        try:
            char_level = int(input("Enter initial level: "))
            if char_level > 0:
                break
            else:
                print("Level must be a positive integer.")
        except ValueError:
            print("Please enter a valid integer for level.")

    player = Character(name, class_type, char_level)

    print("\nCharacter created!")
    player.display_info()

    while True:
        choice = input("\nDo you want to level up? (yes/no): ").lower()
        if choice == "yes":
            player.level_up()
            print("\nUpdated Character info:")
            player.display_info()
        elif choice == "no":
            print("\nFinal Character info:")
            player.display_info()
            break
        else:
            print("Invalid input! Please enter yes or no.")
    
        
        
