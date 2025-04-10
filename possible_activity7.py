import re

class UserProfile:
    def __init__(self, username, email, age):
        self.set_username(username)
        self.set_email(email)
        self.set_age(age)

    # Setter for username
    def set_username(self, username):
        self.__username = username

    # Getter for username
    def get_username(self):
        return self.__username

    # Setter for email with basic validation
    def set_email(self, email):
        if "@" not in email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")
        self.__email = email

    # Getter for email
    def get_email(self):
        return self.__email

    # Setter for age with validation
    def set_age(self, age):
        if age < 13:
            raise ValueError("Age must be 13 or older.")
        self.__age = age

    # Getter for age
    def get_age(self):
        return self.__age

    # Method to display user profile details
    def display_profile(self):
        print(f"Username: {self.__username}")
        print(f"Email: {self.__email}")
        print(f"Age: {self.__age}")


# Example usage with user interaction
if __name__ == "__main__":
    try:
        # Create a user profile
        username = input("Enter username: ")
        email = input("Enter email: ")
        age = int(input("Enter age: "))

        user = UserProfile(username, email, age)
        print("\nUser Profile:")
        user.display_profile()

        # Ask user if they want to update details
        update = input("\nDo you want to update any details? (yes/no): ").strip().lower()
        if update == "yes":
            field = input("Which field do you want to update? (username/email/age): ").strip().lower()
            if field == "username":
                new_username = input("Enter new username: ")
                user.set_username(new_username)
            elif field == "email":
                new_email = input("Enter new email: ")
                try:
                    user.set_email(new_email)
                except ValueError as e:
                    print(f"Error: {e}")
            elif field == "age":
                new_age = int(input("Enter new age: "))
                try:
                    user.set_age(new_age)
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Invalid field.")
            
            print("\nUpdated User Profile:")
            user.display_profile()
        else:
            print("\nNo changes made to the profile.")
    except ValueError as e:
        print(f"Error: {e}")


# User Profile with Age Restrictions
# Problem: Create a UserProfile class with fields: username, email, age.
# Only allow setting age ≥ 13.
# Use getters/setters for all fields.

# Twist: Reject invalid email format (basic validation like checking for '@').