import re

class Account:
    def __init__(self, username, password, account_number, balance):
        self.username = username
        self.password = password
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []
        self.is_locked = False  
        self.last_deposit = 0  # Track last deposit for fraud detection

    def add_transaction(self, transaction):
        self.transaction_history.append(transaction)

    def deposit(self, amount):
        if self.is_locked:
            print("Account is locked. Please contact the bank for verification.")
            return
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        previous_balance = self.balance  # Store previous balance before deposit
        self.balance += amount
        self.last_deposit = amount  # Update last deposit

        transaction = f"Deposited {amount}. New balance: {self.balance}"
        self.add_transaction(transaction)
        print(transaction)

        # Check if deposit is suspicious
        if amount > (previous_balance * 0.5):
            print("🚨 Suspicious transaction detected: Deposit is more than 50% of previous balance.")
            self.is_locked = True

    def withdraw(self, amount):
        if self.is_locked:
            print("Account is locked. Please contact the bank for verification.")
            return
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            print("Insufficient funds.")
            return

        self.balance -= amount
        transaction = f"Withdrew {amount}. New balance: {self.balance}"
        self.add_transaction(transaction)
        print(transaction)

        # Check if withdrawal is suspicious
        if self.balance == 102:
            print("🚨 Suspicious transaction detected: Withdrawal leaves exactly 102 units in the account.")
            self.is_locked = True

        if amount == 3 * self.last_deposit:
            print("🚨 Suspicious transaction detected: Withdrawal is exactly three times the last deposit.")
            self.is_locked = True

    def transfer(self, recipient, amount):
        if self.is_locked:
            print("🚨 Account is locked. Cannot transfer funds.")
            return
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > self.balance:
            print("Insufficient funds.")
            return

        self.balance -= amount
        recipient.balance += amount
        transaction = f"Transferred {amount} to {recipient.account_number}. New balance: {self.balance}"
        self.add_transaction(transaction)
        recipient.add_transaction(f"Received {amount} from {self.account_number}. New balance: {recipient.balance}")
        print(transaction)

    def display_transaction_history(self):
        if not self.transaction_history:
            print("No transactions found.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)

    def display_info(self):
        print(f"Account Number: {self.account_number}, Username: {self.username}, Balance: {self.balance}")


class BankManagementSystem:
    def __init__(self):
        self.accounts = []
        self.manager = Account("admin", "admin", "102000", 0)
        self.accounts.append(self.manager)

    def add_account(self):
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        account_number = input("Enter Account Number (102XXX format): ")

        if not re.fullmatch(r"102\d{3}", account_number):
            print("❌ Invalid account number. It must be in the format 102XXX where X is a digit.")
            return

        balance = float(input("Enter Initial Balance: "))
        new_account = Account(username, password, account_number, balance)
        self.accounts.append(new_account)
        print(f"✅ Account created successfully! Account Number: {account_number}")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def transaction_history(self):
        for account in self.accounts:
            print(f"\nTransaction history for Account Number: {account.account_number}")
            account.display_transaction_history()

    def login_menu(self):
        print("\n🔐 Login Menu")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        account_number = input("Enter Account Number: ")

        for account in self.accounts:
            if account.username == username and account.password == password and account.account_number == account_number:
                print("✅ Login successful!")
                if account.account_number == "102000" and account.username == "admin":
                    self.manager_menu()
                else:
                    self.account_menu(account)
                return
        print("❌ Invalid credentials. Please try again.")

    def account_menu(self, account):
        while True:
            print("\n🏦 Account Menu")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transfer")
            print("5. Transaction History")
            print("6. Logout")

            choice = input("Enter your choice: ")
            if choice == "1":
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == "3":
                print(f"Current balance: {account.balance}")
            elif choice == "4":
                recipient_account_number = input("Enter recipient account number: ")
                recipient = self.find_account(recipient_account_number)
                if recipient:
                    amount = float(input("Enter amount to transfer: "))
                    account.transfer(recipient, amount)
                else:
                    print("❌ Recipient account not found.")
            elif choice == "5":
                account.display_transaction_history()
            elif choice == "6":
                print("🔒 Logging out...")
                break
            else:
                print("❌ Invalid choice. Please try again.")

    def unlock_account(self):
        account_number = input("Enter account number to unlock: ")
        account = self.find_account(account_number)
        if account and account.is_locked:
            account.is_locked = False
            print(f"✅ Account {account_number} has been unlocked.")
        else:
            print("❌ Account not found or not locked.")

    def manager_menu(self):
        while True:
            print("\n👨‍💼 Manager Menu")
            print("1. Add Account")
            print("2. View All Accounts")
            print("3. View Transaction History")
            print("4. Unlock Account")
            print("5. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_account()
            elif choice == "2":
                for account in self.accounts:
                    account.display_info()
            elif choice == "3":
                self.transaction_history()
            elif choice == "4":
                self.unlock_account()
            elif choice == "5":
                print("🔴 Exiting Manager System.")
                break
            else:
                print("❌ Invalid choice. Please try again.")

    def main_menu(self):
        while True:
            print("\n🏦 Welcome to NUD Bank Management System")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_account()
            elif choice == "2":
                self.login_menu()
            elif choice == "3":
                print("🔴 Exiting the system. Thank you for using NUD Bank!")
                break
            else:
                print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    bank_system = BankManagementSystem()
    bank_system.main_menu()
