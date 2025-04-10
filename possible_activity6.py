class TrainTicket:
    def __init__(self, passenger_name, destination, fare):
        self.__passenger_name = passenger_name  # Private attribute
        self.__destination = destination  # Private attribute
        self.__fare = fare  # Private attribute

        # Validate fare during initialization
        if fare < 0:
            raise ValueError("Fare must be non-negative.")

    # Getter for fare
    def get_fare(self):
        return self.__fare

    # Setter for fare with validation
    def set_fare(self, fare):
        if fare < 0:
            raise ValueError("Fare must be non-negative.")
        self.__fare = fare

    # Method to calculate discounted fare
    def calculate_discounted_fare(self):
        if self.__fare > 500:
            return self.__fare * 0.9  # 10% discount
        return self.__fare

    # Method to display ticket details
    def display_ticket_details(self):
        discounted_fare = self.calculate_discounted_fare()
        print(f"Passenger Name: {self.__passenger_name}")
        print(f"Destination: {self.__destination}")
        print(f"Original Fare: {self.__fare}")
        if discounted_fare < self.__fare:
            print(f"Discounted Fare: {discounted_fare}")
        else:
            print("No discount applied.")


# Example usage with user interaction
if __name__ == "__main__":
    try:
        # Create a train ticket
        passenger_name = input("Enter passenger name: ")
        destination = input("Enter destination: ")
        fare = float(input("Enter fare: "))

        ticket = TrainTicket(passenger_name, destination, fare)
        print("\nTicket Details:")
        ticket.display_ticket_details()

        # Ask user if they want to update the fare
        update_fare = input("\nDo you want to update the fare? (yes/no): ").strip().lower()
        if update_fare == "yes":
            new_fare = float(input("Enter new fare: "))
            try:
                ticket.set_fare(new_fare)
                print("\nUpdated Ticket Details:")
                ticket.display_ticket_details()
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("\nNo changes made to the fare.")
    except ValueError as e:
        print(f"Error: {e}")


# Train Reservation System (Based on PDF Example)
# Problem: Create a TrainTicket class (just like the PDF):
# Private fields: passengerName, destination, fare.
# Include validation for fare (must be ≥ 0).

# Twist: Add a calculateDiscountedFare() method if fare > 500 (e.g., 10% discount).