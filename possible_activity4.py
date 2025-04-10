class CartItem:
    def __init__(self, item_name, price, quantity):
        self.__item_name = item_name  # Private attribute
        self.__price = price  # Private attribute
        self.__quantity = quantity  # Private attribute

    # Method to calculate total price for the item
    def get_total_price(self):
        return self.__price * self.__quantity

    # Method to update the quantity
    def update_quantity(self, new_quantity):
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.__quantity = new_quantity

    # Method to display item details
    def display_item_details(self):
        print(f"Item Name: {self.__item_name}")
        print(f"Price: {self.__price}")
        print(f"Quantity: {self.__quantity}")
        print(f"Total Price: {self.get_total_price()}")


# Example usage with user interaction
if __name__ == "__main__":
    cart = []

    while True:
        print("\nOnline Shopping Cart")
        print("1. Add Item to Cart")
        print("2. Update Item Quantity")
        print("3. Display Cart Items")
        print("4. Display Final Bill")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                item_name = input("Enter item name: ")
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                try:
                    cart_item = CartItem(item_name, price, quantity)
                    cart.append(cart_item)
                    print(f"Item '{item_name}' added to cart.")
                except ValueError as e:
                    print(f"Error: {e}")
            elif choice == 2:
                if not cart:
                    print("Cart is empty.")
                else:
                    item_name = input("Enter the name of the item to update: ")
                    for item in cart:
                        if item._CartItem__item_name == item_name:  # Access private attribute
                            new_quantity = int(input("Enter new quantity: "))
                            try:
                                item.update_quantity(new_quantity)
                                print(f"Quantity for '{item_name}' updated.")
                            except ValueError as e:
                                print(f"Error: {e}")
                            break
                    else:
                        print(f"Item '{item_name}' not found in cart.")
            elif choice == 3:
                if not cart:
                    print("Cart is empty.")
                else:
                    print("\nCart Items:")
                    for item in cart:
                        item.display_item_details()
                        print("-" * 30)
            elif choice == 4:
                if not cart:
                    print("Cart is empty.")
                else:
                    total_bill = sum(item.get_total_price() for item in cart)
                    print(f"Final Bill: {total_bill}")
            elif choice == 5:
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")


# Online Shopping Cart
# Problem: Create a CartItem class with private fields: itemName, price, quantity.
# Methods:

# getTotalPrice()

# updateQuantity(int newQuantity) – only if newQuantity >= 0

# displayItemDetails()

# Twist: Use an array or list to store multiple cart items and display a final bill.