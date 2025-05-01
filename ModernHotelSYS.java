import java.io.*;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.*;

class Room {
    private int roomNumber;
    private String roomType;
    private double pricePerNight;
    private boolean isAvailable;

    public Room(int roomNumber, String roomType, double pricePerNight, boolean isAvailable) {
        this.roomNumber = roomNumber;
        this.roomType = roomType;
        this.pricePerNight = pricePerNight;
        this.isAvailable = isAvailable;
    }

    public int getRoomNumber() {
        return roomNumber;
    }

    public String getRoomType() {
        return roomType;
    }

    public double getPricePerNight() {
        return pricePerNight;
    }

    public boolean isAvailable() {
        return isAvailable;
    }

    public void setAvailable(boolean available) {
        isAvailable = available;
    }

    @Override
    public String toString() {
        return "Room " + roomNumber + " (" + roomType + ") - $" + pricePerNight + "/night";
    }
}

class Guest {
    private String name;
    private String contactInfo;

    public Guest(String name, String contactInfo) {
        this.name = name;
        this.contactInfo = contactInfo;
    }

    public String getName() {
        return name;
    }

    public String getContactInfo() {
        return contactInfo;
    }

    @Override
    public String toString() {
        return "Guest: " + name + ", Contact: " + contactInfo;
    }
}

class Reservation {
    private String reservationId;
    private Guest guest;
    private Room room;
    private LocalDate checkInDate;
    private LocalDate checkOutDate;

    public Reservation(Guest guest, Room room, LocalDate checkInDate, LocalDate checkOutDate) {
        this.reservationId = UUID.randomUUID().toString();
        this.guest = guest;
        this.room = room;
        this.checkInDate = checkInDate;
        this.checkOutDate = checkOutDate;
    }

    public String getReservationId() {
        return reservationId;
    }

    public Guest getGuest() {
        return guest;
    }

    public Room getRoom() {
        return room;
    }

    public LocalDate getCheckInDate() {
        return checkInDate;
    }

    public LocalDate getCheckOutDate() {
        return checkOutDate;
    }

    public double calculateTotalCost() {
        long numNights = java.time.temporal.ChronoUnit.DAYS.between(checkInDate, checkOutDate);
        return numNights * room.getPricePerNight();
    }

    @Override
    public String toString() {
        return "Reservation ID: " + reservationId + "\n" +
                "Guest: " + guest.getName() + "\n" +
                "Room: " + room.getRoomNumber() + " (" + room.getRoomType() + ")\n" +
                "Check-in: " + checkInDate + ", Check-out: " + checkOutDate + "\n" +
                "Total Cost: $" + calculateTotalCost();
    }
}

class Hotel {
    private String name;
    private String address;
    private List<Room> rooms;
    private List<Reservation> reservations;

    public Hotel(String name, String address) {
        this.name = name;
        this.address = address;
        this.rooms = new ArrayList<>();
        this.reservations = new ArrayList<>();
    }

    public void addRoom(Room room) {
        rooms.add(room);
    }

    public void autoAddRooms(int numSingles, int numDoubles, int numSuites) {
        for (int i = 1; i <= numSingles; i++) {
            addRoom(new Room(100 + i, "Single", 100, true));
        }
        for (int i = 1; i <= numDoubles; i++) {
            addRoom(new Room(200 + i, "Double", 150, true));
        }
        for (int i = 1; i <= numSuites; i++) {
            addRoom(new Room(300 + i, "Suite", 300, true));
        }
    }

    public Room findAvailableRoom(String roomType) {
        for (Room room : rooms) {
            if (room.getRoomType().equalsIgnoreCase(roomType) && room.isAvailable()) {
                return room;
            }
        }
        return null;
    }

    public void listAvailableRooms() {
        boolean hasAvailableRooms = false;
        for (Room room : rooms) {
            if (room.isAvailable()) {
                System.out.println(room);
                hasAvailableRooms = true;
            }
        }
        if (!hasAvailableRooms) {
            System.out.println("No rooms available.");
        }
    }

    public void listReservations() {
        if (reservations.isEmpty()) {
            System.out.println("No current reservations.");
        } else {
            for (Reservation reservation : reservations) {
                System.out.println(reservation);
                System.out.println("----------------------------------------");
            }
        }
    }

    public Reservation makeReservation(Guest guest, String roomType, LocalDate checkInDate, LocalDate checkOutDate) {
        if (!checkInDate.isBefore(checkOutDate)) {
            System.out.println("Error: Check-in date must be before check-out date.");
            return null;
        }

        Room room = findAvailableRoom(roomType);
        if (room != null) {
            room.setAvailable(false);
            Reservation reservation = new Reservation(guest, room, checkInDate, checkOutDate);
            reservations.add(reservation);
            saveReservationsToFile();
            return reservation;
        } else {
            System.out.println("No available rooms for the selected type.");
            return null;
        }
    }

    public void cancelReservation(String reservationId) {
        Iterator<Reservation> iterator = reservations.iterator();
        while (iterator.hasNext()) {
            Reservation reservation = iterator.next();
            if (reservation.getReservationId().equals(reservationId)) {
                reservation.getRoom().setAvailable(true);
                iterator.remove();
                saveReservationsToFile();
                System.out.println("Reservation " + reservationId + " has been canceled.");
                return;
            }
        }
        System.out.println("Reservation ID " + reservationId + " not found.");
    }

    public void saveReservationsToFile() {
        try (PrintWriter writer = new PrintWriter(new File("reservations.csv"))) {
            writer.println("Reservation ID,Guest Name,Room Number,Room Type,Check-in Date,Check-out Date,Total Cost");
            for (Reservation reservation : reservations) {
                writer.println(reservation.getReservationId() + "," +
                        reservation.getGuest().getName() + "," +
                        reservation.getRoom().getRoomNumber() + "," +
                        reservation.getRoom().getRoomType() + "," +
                        reservation.getCheckInDate() + "," +
                        reservation.getCheckOutDate() + "," +
                        reservation.calculateTotalCost());
            }
            System.out.println("Reservations saved to reservations.csv.");
        } catch (IOException e) {
            System.out.println("Error saving reservations to file: " + e.getMessage());
        }
    }

    public void loadReservationsFromFile() {
        try (BufferedReader reader = new BufferedReader(new FileReader("reservations.csv"))) {
            String line = reader.readLine(); // Skip header
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(",");
                String guestName = parts[1];
                String roomType = parts[3];
                LocalDate checkInDate = LocalDate.parse(parts[4]);
                LocalDate checkOutDate = LocalDate.parse(parts[5]);

                Guest guest = new Guest(guestName, "N/A");
                Room room = findAvailableRoom(roomType);
                if (room != null) {
                    room.setAvailable(false);
                    reservations.add(new Reservation(guest, room, checkInDate, checkOutDate));
                }
            }
            System.out.println("Reservations loaded from reservations.csv.");
        } catch (FileNotFoundException e) {
            System.out.println("No existing reservation file found.");
        } catch (IOException e) {
            System.out.println("Error loading reservations from file: " + e.getMessage());
        }
    }
}

public class ModernHotelSYS {
    public static void main(String[] args) {
        Hotel hotel = new Hotel("Modern Hotel", "123 Main Street");
        hotel.autoAddRooms(10, 10, 10);
        hotel.loadReservationsFromFile();

        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("\nWelcome to Modern Hotel Reservation System");
            System.out.println("1. List Available Rooms");
            System.out.println("2. Make a Reservation");
            System.out.println("3. Cancel a Reservation");
            System.out.println("4. View Current Reservations");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    hotel.listAvailableRooms();
                    break;
                case "2":
                    System.out.print("Enter guest name: ");
                    String name = scanner.nextLine();
                    System.out.print("Enter guest contact info: ");
                    String contactInfo = scanner.nextLine();
                    Guest guest = new Guest(name, contactInfo);

                    System.out.print("Enter room type (Single/Double/Suite): ");
                    String roomType = scanner.nextLine();
                    System.out.print("Enter check-in date (YYYY-MM-DD): ");
                    LocalDate checkInDate = LocalDate.parse(scanner.nextLine());
                    System.out.print("Enter check-out date (YYYY-MM-DD): ");
                    LocalDate checkOutDate = LocalDate.parse(scanner.nextLine());

                    Reservation reservation = hotel.makeReservation(guest, roomType, checkInDate, checkOutDate);
                    if (reservation != null) {
                        System.out.println("Reservation successful!");
                        System.out.println(reservation);
                    }
                    break;
                case "3":
                    System.out.print("Enter reservation ID to cancel: ");
                    String reservationId = scanner.nextLine();
                    hotel.cancelReservation(reservationId);
                    break;
                case "4":
                    hotel.listReservations();
                    break;
                case "5":
                    System.out.println("Thank you for using Modern Hotel Reservation System. Goodbye!");
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}
