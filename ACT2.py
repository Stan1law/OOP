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
        return self.__level
        print(f"{self.__name} has leveled up to level {self.__level}")
        
    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Class: {self.__class_type}")
        print(f"Level: {self.__level}")
        
if __name__ == "__main__":
    valid_classes = {"warrior", "mage", "archer"}
    
    name = input("Enter character name: ")
    class_type = input("Enter class type (warrior/mage/archer)")
    while True:
        if class_type not in valid_classes:
            break
        else:
            break
        
    level = int(input("Enter initial level:"))
    
    player = Character(name, class_type, level)
    
    print("\nCharacter details:")
    player.display_info()
    
    while True:
        choice = input("Do you want to level up? (yes/no)")
        if choice.lower() == "yes":
            player.level_up()
            print("Updated Character details:")
            player.display_info()
        elif choice.lower() == "no":
            player.display_info()
            break
        else:
            print("Invalid input!")
            
        
    
    
    
