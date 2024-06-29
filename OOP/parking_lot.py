class Vehicle:
    def __init__(self, license_plate):
        self.license_plate = license_plate


class ParkingSpot:
    def __init__(self, spot_id, size="medium"):
        self.spot_id = spot_id
        self.size = size
        self.is_available = True
        self.vehicle = None

    def park_vehicle(self, vehicle):
        if self.is_available:
            self.vehicle = vehicle
            self.is_available = False
            print(f"Vehicle {vehicle.license_plate} parked at spot {self.spot_id}.")
        else:
            print(f"Spot {self.spot_id} is already occupied.")

    def remove_vehicle(self):
        if not self.is_available:
            print(f"Vehicle {self.vehicle.license_plate} left spot {self.spot_id}.")
            self.vehicle = None
            self.is_available = True
        else:
            print(f"Spot {self.spot_id} is already empty.")


class ParkingLot:
    def __init__(self):
        self.spots = {}

    def add_parking_spot(self, spot_id, size="medium"):
        if spot_id in self.spots:
            print(f"Spot {spot_id} already exists.")
        else:
            self.spots[spot_id] = ParkingSpot(spot_id, size)
            print(f"Spot {spot_id} added as a {size} spot.")

    def park_vehicle(self, spot_id, vehicle):
        if spot_id in self.spots:
            self.spots[spot_id].park_vehicle(vehicle)
        else:
            print(f"Spot {spot_id} does not exist.")

    def remove_vehicle(self, spot_id):
        if spot_id in self.spots:
            self.spots[spot_id].remove_vehicle()
        else:
            print(f"Spot {spot_id} does not exist.")

    def get_available_spots(self):
        available_spots = [
            spot_id for spot_id, spot in self.spots.items() if spot.is_available
        ]
        return available_spots


# Example usage
parking_lot = ParkingLot()
parking_lot.add_parking_spot("A1", "small")
parking_lot.add_parking_spot("A2", "medium")
parking_lot.add_parking_spot("A3", "large")

vehicle1 = Vehicle("ABC123")
vehicle2 = Vehicle("XYZ789")

parking_lot.park_vehicle("A1", vehicle1)
parking_lot.park_vehicle("A2", vehicle2)

print("Available spots:", parking_lot.get_available_spots())

parking_lot.remove_vehicle("A1")
parking_lot.remove_vehicle("A2")

print("Available spots:", parking_lot.get_available_spots())
