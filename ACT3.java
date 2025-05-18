import java.util.Scanner;
class Calculator{
    private String secretPasscode;
    
    public Calculator(String passcode){
        this.secretPasscode = passcode;
    }
    
    private boolean unlockSecret(String passcode){
        return this.secretPasscode.equals(passcode);
    }
    
    public double add(double a, double b){
        return a + b;
    }
    
    public double subtract(double a, double b){
        return a - b;
    }
    
    public double multiply(double a, double b){
        return a * b;
    }
    
    public String divide(double a, double b){
        if (b != 0){
            return String.valueOf(a / b);
        } else {
            return "Error: Division by zero";
        }
    }
    
    public String power(double a, double b, String passcode){
        if (unlockSecret(passcode)){
            return String.valueOf(Math.pow(a, b));
        } else {
            return "Access denied. We are proceeding with basic operations only!";
        }
    }
}


class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a new passcode to unlok secret operation: ");
        String userPasscode = scanner.nextLine();
        
        Calculator calc = new Calculator(userPasscode);
        
        System.out.print("Enter first number: ");
        double a = scanner.nextDouble();
        
        System.out.print("Enter second number: ");
        double b = scanner.nextDouble();
       
        
        System.out.println("\nChoose an operation:");
        System.out.println("1- ADD");
        System.out.println("2 - SUBTRACT");
        System.out.println("3 - MULTIPLY");
        System.out.println("4 - DIVIDE");
        System.out.println("5 - POWER (Secret Operation)");
        
        System.out.print("Enter your choice: ");
        String choice = scanner.nextLine();
        
        String result;
        
        switch (choice){
            case "1":
                result = String.valueOf(calc.add(a, b));
            case "2":
                result = String.valueOf(calc.subtract(a, b));
            case "3":
                result = String.valueOf(calc.multiply(a, b));
            case "4":
                result = String.valueOf(calc.divide(a, b));
            case "5":
                scanner.nextLine();
                System.out.print("\nEnter passcode to Unlock the secret operation: ");
                String passcode = scanner.nextLine();
                result = calc.power(a, b , passcode);
                break;
            default:
                result = "Invalid choice!";
        }
        
        System.out.println("\nResult: "+ result);
        
        
    }
}
