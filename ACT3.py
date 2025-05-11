class Calculator:
    def __init__(self, passcode):
        self.__secretPasscode = passcode
        
    def unlock_secret(self, passcode):
        return passcode == self.__secretPasscode
        
    def add(self, a, b):
        return a + b
        
    def subtract(self, a, b):
        return a - b
        
    def multiply(self, a, b):
        return a * b
        
    def divide(self, a, b):
        return a / b if b != 0 else "Error: Division by zero"
        
    def power(self, a, b, passcode):
        if self.unlock_secret(passcode):
            return a ** b
        else:
            return "Access Denied. We are proceeding with basic opeartions only."
    
    
def main():
    user_passcode = input("Enter the passcode to unlock the secret operation: ")
    
    calc = Calculator(user_passcode)
    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    print("\n\nChoose an operation:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("5 - Power (Secret Operation)")
        
    choice = (input("Enter your choice: "))
    
    if choice in ['1', '2', '3', '4', '5']:
        
        if choice == '1':
            result = calc.add(a, b)
        elif choice == '2':
            result = calc.subtract(a, b)
        elif choice == '3':
            result = calc.multiply(a, b)
        elif choice == '4':
            result = calc.divide(a, b)
        elif choice == '5':
            passcode = input("\nEnter passcode to unlock the secret opeartion: ")
            result = calc.power(a, b, passcode)
            
        print(f"\nResult: {result}")
        
    else:
        print("Invalid choice!")
        
if __name__ == "__main__":
        main()
    
        
            
    
    
    
    
    
    
    
    
    
    
