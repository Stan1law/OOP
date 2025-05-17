import java.util.Scanner;

class Character{
    private String name;
    private String classType;
    private int level;
    
    public Character(String name, String classType, int level){
        this.name = name;
        this.classType = classType;
        this.level = level;
    }
    
    public String getName(){
        return name;
    }
    
    public String getClassType(){
        return classType;
    }
    
    public int getLevel(){
        return level;
    }
    
    public void levelUp(){
        level++;
        System.out.println(name + "has level up to level " + level);
    }
    
    public void displayInfo(){
        System.out.println("Name: " + name);
        System.out.println("Class: " + classType);
        System.out.println("Level: " + level);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter character name: ");
        String name = scanner.nextLine();
        
        String classType;
        while (true){
            System.out.print("Enter class type (warrior/mage/archer): ");
            classType = scanner.nextLine().toLowerCase();
            
            if (!classType.equals("warrior") && !classType.equals("mage") && !classType.equals("archer")){
                System.out.println("Invalid Input");
            } else {
                break;
            }
            
        }
        
        System.out.print("Enter initial level: ");
        int level = scanner.nextInt();
        scanner.nextLine();
        
        Character player = new Character(name, classType, level);
        
        System.out.print("\nCharater details:");
        player.displayInfo();
        
        while (true){
            System.out.print("do you want to level up? (yes/no): ");
            String choice = scanner.nextLine().toLowerCase();
            if (choice.equals("yes")){
                player.levelUp();
                player.displayInfo();
            } else if (choice.equals("no")){
                player.displayInfo();
                break;
            } else {
                System.out.println("Invalid input");
            }
        }
        
    }
}
