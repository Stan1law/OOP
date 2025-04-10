class Book:
    def __init__(self, title, author, price):
        self.__title = title  # Private attribute
        self.__author = author  # Private attribute
        self.__price = price  # Private attribute

    # Setter for price with validation
    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = price

    # Getter for price
    def get_price(self):
        return self.__price

    # Method to display book details
    def display_details(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Price: {self.__price}")


# Example usage with user interaction
if __name__ == "__main__":
    # Create a book object
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    price = float(input("Enter book price: "))

    try:
        book = Book(title, author, price)
        print("\nBook Details:")
        book.display_details()

        # Ask user if they want to update the price
        update_price = input("\nDo you want to update the price? (yes/no): ").strip().lower()
        if update_price == "yes":
            new_price = float(input("Enter new price: "))
            try:
                book.set_price(new_price)
                print("\nUpdated Book Details:")
                book.display_details()
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("\nNo changes made to the price.")
    except ValueError as e:
        print(f"Error: {e}")


# Encapsulation + Constructors Combo
# Problem: Combine encapsulation and constructors in a Book class:
# Private attributes: title, author, price.
# Constructor initializes all fields.
# Setter method for price should validate non-negative value.
# Display method shows all details.

# Twist: Ask user if they want to change the price via setPrice() and show updated details.