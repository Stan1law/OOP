class Product:
    def __init__(self, product_id, product_name, quantity=0):
        self.__product_id = product_id  # Private attribute
        self.__product_name = product_name  # Private attribute
        self.__quantity = quantity  # Private attribute

    # Method to add stock
    def add_stock(self, amount):
        if amount <= 0:
            raise ValueError("Stock amount to add must be positive.")
        self.__quantity += amount
        print(f"Added {amount} units. New quantity: {self.__quantity}")

    # Method to reduce stock
    def reduce_stock(self, amount):
        if amount <= 0:
            raise ValueError("Stock amount to reduce must be positive.")
        if amount > self.__quantity:
            raise ValueError("Insufficient stock to reduce.")
        self.__quantity -= amount
        print(f"Reduced {amount} units. New quantity: {self.__quantity}")

    # Method to display product information
    def display_product_info(self):
        print(f"Product ID: {self.__product_id}")
        print(f"Product Name: {self.__product_name}")
        print(f"Quantity: {self.__quantity}")


# Example usage with user interaction
if __name__ == "__main__":
    # Create a product
    product = Product("P001", "Laptop", 50)

    while True:
        print("\nInventory Management System")
        print("1. Display Product Info")
        print("2. Add Stock")
        print("3. Reduce Stock")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                product.display_product_info()
            elif choice == 2:
                amount = int(input("Enter amount to add: "))
                product.add_stock(amount)
            elif choice == 3:
                amount = int(input("Enter amount to reduce: "))
                product.reduce_stock(amount)
            elif choice == 4:
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")


# nventory System Problem: Create a Product class with private attributes: productId, productName, and quantity. Methods:

# addStock(int amount)

# reduceStock(int amount) – only reduce if amount <= quantity

# displayProductInfo()

# Twist: Allow user input and let the user add/reduce stock in a loop.