import csv
import datetime
import uuid

# Define the Room class
class Room:
    def __init__(self, room_number, room_type, price_per_night, is_available=True):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = is_available

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type}) - ${self.price_per_night}/night"

# Define the Guest class
class Guest:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def __str__(self):
        return f"Guest: {self.name}, Contact: {self.contact_info}"

# Define the Reservation class
class Reservation:
    def __init__(self, guest, room, check_in_date, check_out_date):
        self.reservation_id = str(uuid.uuid4())  # Generate a unique reservation ID
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def calculate_total_cost(self):
        num_nights = (self.check_out_date - self.check_in_date).days
        return num_nights * self.room.price_per_night

    def __str__(self):
        return (f"Reservation ID: {self.reservation_id}\n"
                f"Guest: {self.guest.name}\n"
                f"Room: {self.room.room_number} ({self.room.room_type})\n"
                f"Check-in: {self.check_in_date}, Check-out: {self.check_out_date}\n"
                f"Total Cost: ${self.calculate_total_cost()}")

# Define the Hotel class
class Hotel:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.rooms = []
        self.reservations = []

    def add_room(self, room):
        self.rooms.append(room)

    def auto_add_rooms(self, num_singles, num_doubles, num_suites):
        for i in range(1, num_singles + 1):
            self.add_room(Room(100 + i, "Single", 100))
        for i in range(1, num_doubles + 1):
            self.add_room(Room(200 + i, "Double", 150))
        for i in range(1, num_suites + 1):
            self.add_room(Room(300 + i, "Suite", 300))

    def find_available_room(self, room_type):
        for room in self.rooms:
            if room.room_type.lower() == room_type.lower() and room.is_available:
                return room
        return None

    def list_available_rooms(self):
        available_rooms = [room for room in self.rooms if room.is_available]
        if available_rooms:
            print("Available Rooms:")
            for room in available_rooms:
                print(room)
        else:
            print("No rooms available.")

    def list_reservations(self):
        if self.reservations:
            print("\nCurrent Reservations:")
            for reservation in self.reservations:
                print(reservation)
                print("-" * 40)
        else:
            print("No current reservations.")

    def make_reservation(self, guest, room_type, check_in_date, check_out_date):
        if check_in_date >= check_out_date:
            print("Error: Check-in date must be before check-out date.")
            return None

        room = self.find_available_room(room_type)
        if room:
            room.is_available = False
            reservation = Reservation(guest, room, check_in_date, check_out_date)
            self.reservations.append(reservation)
            self.save_reservations_to_file()  # Save reservations to file
            return reservation
        else:
            print("No available rooms for the selected type.")
            return None

    def cancel_reservation(self, reservation_id):
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                confirm = input(f"Are you sure you want to cancel reservation {reservation_id}? (yes/no): ").lower()
                if confirm != "yes":
                    print("Cancellation aborted.")
                    return

                reservation.room.is_available = True
                self.reservations.remove(reservation)
                self.save_reservations_to_file()  # Save reservations to file
                print(f"Reservation {reservation_id} has been canceled.")
                return
        print(f"Reservation ID {reservation_id} not found.")

    def __str__(self):
        return f"{self.name}, located at {self.address}"

    def save_reservations_to_file(self, filename="reservations.csv"):
        """Save all reservations to a CSV file."""
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Reservation ID", "Guest Name", "Room Number", "Room Type", "Check-in Date", "Check-out Date", "Total Cost"])
            for reservation in self.reservations:
                writer.writerow([
                    reservation.reservation_id,
                    reservation.guest.name,
                    reservation.room.room_number,
                    reservation.room.room_type,
                    reservation.check_in_date,
                    reservation.check_out_date,
                    reservation.calculate_total_cost()
                ])
        print(f"Reservations saved to {filename}.")

    def load_reservations_from_file(self, filename="reservations.csv"):
        """Load reservations from a CSV file (optional feature)."""
        try:
            with open(filename, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    guest = Guest(row["Guest Name"], "N/A")
                    room = self.find_available_room(row["Room Type"])
                    if room:
                        room.is_available = False
                        check_in_date = datetime.datetime.strptime(row["Check-in Date"], "%Y-%m-%d").date()
                        check_out_date = datetime.datetime.strptime(row["Check-out Date"], "%Y-%m-%d").date()
                        reservation = Reservation(guest, room, check_in_date, check_out_date)
                        self.reservations.append(reservation)
            print(f"Reservations loaded from {filename}.")
        except FileNotFoundError:
            print(f"No existing reservation file found: {filename}.")


def main():
    hotel = Hotel("Modern Hotel", "123 Main Street")
    hotel.auto_add_rooms(10, 10, 10)
    hotel.load_reservations_from_file()

    while True:
        print("\nWelcome to Modern Hotel Reservation System")
        print("1. List Available Rooms")
        print("2. Make a Reservation")
        print("3. Cancel a Reservation")
        print("4. View Current Reservations")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            hotel.list_available_rooms()
        elif choice == "2":
            name = input("Enter guest name: ")
            contact_info = input("Enter guest contact info: ")
            guest = Guest(name, contact_info)

            valid_room_types = ["Single", "Double", "Suite"]
            room_type_input = input("Enter room type (Single/Double/Suite): ").title()
            if room_type_input not in valid_room_types:
                print("Invalid room type. Please enter Single, Double, or Suite.")
                continue

            try:
                check_in_str = input("Enter check-in date (MM/DD): ")
                check_out_str = input("Enter check-out date (MM/DD): ")
                current_year = datetime.date.today().year
                check_in_date = datetime.datetime.strptime(f"{check_in_str}/{current_year}", "%m/%d/%Y").date()
                check_out_date = datetime.datetime.strptime(f"{check_out_str}/{current_year}", "%m/%d/%Y").date()
            except ValueError:
                print("Invalid date format. Please use MM/DD.")
                continue

            reservation = hotel.make_reservation(guest, room_type_input, check_in_date, check_out_date)
            if reservation:
                print("Reservation successful!")
                print(reservation)
        elif choice == "3":
            reservation_id = input("Enter reservation ID to cancel: ")
            hotel.cancel_reservation(reservation_id)
        elif choice == "4":
            hotel.list_reservations()
        elif choice == "5":
            print("Thank you for using Modern Hotel Reservation System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
