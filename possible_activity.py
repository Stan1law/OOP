class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.__account_number = account_number  # Private attribute
        self.__account_holder = account_holder  # Private attribute
        self.__balance = balance  # Private attribute

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Getter for account holder
    def get_account_holder(self):
        return self.__account_holder

    # Setter for account holder with validation
    def set_account_holder(self, name):
        if not name.isalpha():
            raise ValueError("Account holder name must contain only letters.")
        self.__account_holder = name

    # Deposit method
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        print(f"Withdrew {amount}. New balance: {self.__balance}")


# Example usage
if __name__ == "__main__":
    # Create a bank account
    account = BankAccount("123456", "JohnDoe", 1000.0)

    # Get account details
    print("Account Holder:", account.get_account_holder())
    print("Balance:", account.get_balance())

    # Update account holder name
    try:
        account.set_account_holder("JaneDoe")
        print("Updated Account Holder:", account.get_account_holder())
    except ValueError as e:
        print(e)

    # Deposit money
    try:
        account.deposit(500)
    except ValueError as e:
        print(e)

    # Withdraw money
    try:
        account.withdraw(300)
    except ValueError as e:
        print(e)

    # Attempt invalid operations
    try:
        account.set_account_holder("John123")  # Invalid name
    except ValueError as e:
        print(e)

    try:
        account.withdraw(2000)  # Insufficient funds
    except ValueError as e:
        print(e)


# Bank Account Class (Classic Exercise) Problem: Create a BankAccount class with private attributes: accountNumber, accountHolder, and balance. Methods:

# getBalance(), getAccountHolder()

# setAccountHolder(String name)

# deposit(double amount) – adds to balance

# withdraw(double amount) – subtracts from balance only if sufficient funds

# Challenge twist: Add validation in setAccountHolder (e.g., no numbers allowed in names).