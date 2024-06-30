"""
UML Diagram: Parking Lot

+--------------------+
|      Vehicle       |
+--------------------+
| - license_plate    |
| - vehicle_type     |
+--------------------+
| + __init__()       |
| + __str__()        |
+--------------------+
          ^
          |
          |
       inherits
          |
+--------------------+
|        Car         |
+--------------------+
| + __init__()       |
+--------------------+
          ^
          |
          |
       inherits
          |
+--------------------+
|    Motorcycle      |
+--------------------+
| + __init__()       |
+--------------------+

+--------------------+
|   ParkingSpot      |
+--------------------+
| - spot_number      |
| - spot_size        |
| - vehicle          |
+--------------------+
| + __init__()       |
| + is_available()   |
| + can_fit_vehicle()|
| + park_vehicle()   |
| + remove_vehicle() |
+--------------------+

+--------------------+
|    ParkingLot      |
+--------------------+
| - spots            |
+--------------------+
| + __init__()       |
| + find_available_spot()|
| + park_vehicle()   |
| + remove_vehicle() |
+--------------------+

"""


class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

    def __str__(self):
        return f"{self.vehicle_type} with license plate {self.license_plate}"


class Car(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, "Car")


class Motorcycle(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, "Motorcycle")


class ParkingSpot:
    def __init__(self, spot_number, spot_size):
        self.spot_number = spot_number
        self.spot_size = spot_size
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None

    def can_fit_vehicle(self, vehicle):
        # For simplicity, we assume motorcycle can fit in any spot, and car in car or larger spots
        if vehicle.vehicle_type == "Motorcycle":
            return True
        elif vehicle.vehicle_type == "Car" and self.spot_size == "Car":
            return True
        return False

    def park_vehicle(self, vehicle):
        if self.is_available() and self.can_fit_vehicle(vehicle):
            self.vehicle = vehicle
            print(f"Parked {vehicle} at spot {self.spot_number}")
        else:
            print(f"Cannot park {vehicle} at spot {self.spot_number}")

    def remove_vehicle(self):
        if not self.is_available():
            vehicle = self.vehicle
            self.vehicle = None
            print(f"Removed {vehicle} from spot {self.spot_number}")
            return vehicle
        else:
            print(f"Spot {self.spot_number} is already empty")
            return None


class ParkingLot:
    def __init__(self, num_car_spots, num_motorcycle_spots):
        self.spots = []
        self.spots.extend([ParkingSpot(i, "Car") for i in range(1, num_car_spots + 1)])
        self.spots.extend(
            [
                ParkingSpot(i + num_car_spots, "Motorcycle")
                for i in range(1, num_motorcycle_spots + 1)
            ]
        )

    def find_available_spot(self, vehicle):
        for spot in self.spots:
            if spot.is_available() and spot.can_fit_vehicle(vehicle):
                return spot
        return None

    def park_vehicle(self, vehicle):
        spot = self.find_available_spot(vehicle)
        if spot:
            spot.park_vehicle(vehicle)
        else:
            print("No available spots for this vehicle")

    def remove_vehicle(self, license_plate):
        for spot in self.spots:
            if spot.vehicle and spot.vehicle.license_plate == license_plate:
                spot.remove_vehicle()
                return
        print(f"No vehicle with license plate {license_plate} found in the lot")


if __name__ == "__main__":
    # Example usage
    parking_lot = ParkingLot(num_car_spots=3, num_motorcycle_spots=2)

    car1 = Car("ABC123")
    car2 = Car("XYZ789")
    motorcycle1 = Motorcycle("MOTO123")

    parking_lot.park_vehicle(car1)
    parking_lot.park_vehicle(car2)
    parking_lot.park_vehicle(motorcycle1)

    parking_lot.remove_vehicle("ABC123")
    parking_lot.remove_vehicle("XYZ789")
    parking_lot.remove_vehicle("MOTO123")
