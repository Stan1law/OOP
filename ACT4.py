class Vehicle:
    def __init__(self, brand, model, distance, fuel_used):
        self.__brand = brand
        self.__model = model
        self.__distance = distance
        self.__fuel_used = fuel_used
        
    def get_brand(self):
        return self.__brand
        
    def get_model(self):
        return self.__model
        
    def get_distance(self):
        return self.__distance
        
    def get_fuel_used(self):
        return self.__fuel_used
        
    def calculate_fuel_efficiency(self):
        if self.__fuel_used == 0:
            return 0
        return self.__distance/self.__fuel_used
        
    def display_summary(self):
        print(f"Vehicle: {self.__brand}{self.__model}")
        print(f"Distance Traveled: {self.__distance:.1f}km")
        print(f"Fuel Efficiency: {self.calculate_fuel_efficiency():.2f} km/l\n")
        
class Car(Vehicle):
    pass

class Bike(Vehicle):
    def __init__(self, brand, model, distance):
        super().__init__(brand, model, distance, 1.5)

class Truck(Vehicle):
    pass
    
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value< 0:
                print("value must be non-negative.")
                continue
            return value
        except ValueError:
            print("Please enter valid number!")
        
def main():
    print("Enter details for a Car")
    car_brand = input("Brand: ")
    car_model = input("Model: ")
    car_distance = get_positive_float("Distance Traveled (km): ")
    car_fuel = get_positive_float("Fuel Used (liters): ")
    car = Car(car_brand, car_model, car_distance, car_fuel)
    
    print("\n\nEnter details for a Bike")
    bike_brand = input("Brand: ")
    bike_model = input("Model: ")
    bike_distance = get_positive_float("Distance Traveled (km): ")
    bike = Bike(bike_brand, bike_model, bike_distance)
    
    print("\n\nEnter details for a Truck")
    truck_brand = input("Brand: ")
    truck_model = input("Model: ")
    truck_distance = get_positive_float("Distance Traveled (km): ")
    truck_fuel = get_positive_float("Fuel Used (liters): ")
    truck = Truck(truck_brand, truck_model, truck_distance, truck_fuel)
    
    print("\n--- Vehicle Summary ---")
    car.display_summary()
    bike.display_summary()
    truck.display_summary()
    
if __name__ == "__main__":
    main()
    
    
