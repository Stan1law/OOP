class Room:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = True

    def book(self):
        if not self.is_available:
            raise Exception(f"Room {self.room_number} is already booked.")
        self.is_available = False

    def release(self):
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Booked"
        return f"Room {self.room_number}: {self.room_type} - ${self.price_per_night}/night ({status})"


class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact


class Reservation:
    def __init__(self, reservation_id, customer, room, nights):
        self.reservation_id = reservation_id
        self.customer = customer
        self.room = room
        self.nights = nights
        self.total_price = room.price_per_night * nights

    def __str__(self):
        return (f"Reservation ID: {self.reservation_id}\n"
                f"Customer: {self.customer.name}, Contact: {self.customer.contact}\n"
                f"Room: {self.room.room_number} ({self.room.room_type})\n"
                f"Nights: {self.nights}, Total Price: ${self.total_price}")


class HotelReservationSystem:
    def __init__(self):
        self.rooms = []
        self.reservations = {}
        self.reservation_counter = 1

    def add_room(self, room_number, room_type, price_per_night):
        self.rooms.append(Room(room_number, room_type, price_per_night))
        print(f"Room {room_number} added.")

    def display_available_rooms(self):
        print("\nAvailable Rooms:")
        available = False
        for room in self.rooms:
            if room.is_available:
                print(room)
                available = True
        if not available:
            print("No rooms available.")

    def make_reservation(self, name, contact, room_number, nights):
        customer = Customer(name, contact)
        for room in self.rooms:
            if room.room_number == room_number:
                if room.is_available:
                    room.book()
                    reservation_id = f"RES-{self.reservation_counter}"
                    self.reservation_counter += 1
                    reservation = Reservation(reservation_id, customer, room, nights)
                    self.reservations[reservation_id] = reservation
                    print(f"Reservation successful! ID: {reservation_id}")
                    return
                else:
                    print(f"Room {room_number} is already booked.")
                    return
        print(f"Room {room_number} not found.")

    def cancel_reservation(self, reservation_id):
        reservation = self.reservations.pop(reservation_id, None)
        if reservation:
            reservation.room.release()
            print(f"Reservation {reservation_id} cancelled.")
        else:
            print("Reservation ID not found.")

    def display_reservations(self):
        print("\nCurrent Reservations:")
        if not self.reservations:
            print("No reservations found.")
        for reservation in self.reservations.values():
            print(reservation)
            print("-" * 40)


if __name__ == "__main__":
    system = HotelReservationSystem()

    # Sample rooms
    system.add_room(101, "Single", 100)
    system.add_room(102, "Double", 150)
    system.add_room(201, "Suite", 300)

    while True:
        print("\nHotel Reservation System")
        print("1. Show Available Rooms")
        print("2. Make a Reservation")
        print("3. Cancel a Reservation")
        print("4. Show All Reservations")
        print("5. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            system.display_available_rooms()
        elif choice == 2:
            name = input("Customer name: ")
            contact = input("Customer contact: ")
            try:
                room_number = int(input("Room number: "))
                nights = int(input("Number of nights: "))
                system.make_reservation(name, contact, room_number, nights)
            except ValueError:
                print("Invalid room number or nights.")
        elif choice == 3:
            res_id = input("Enter reservation ID to cancel: ")
            system.cancel_reservation(res_id)
        elif choice == 4:
            system.display_reservations()
        elif choice == 5:
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
