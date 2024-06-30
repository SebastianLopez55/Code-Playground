"""
UML Diagram: Parking Lot

+--------------------+
|      Vehicle       |
+--------------------+
| - license_plate    |
+--------------------+
| + __init__()       |
+--------------------+
          ^
          |
          |
       inherits
          |
+--------------------+
|        Car         |
+--------------------+
| - make             |
| - model            |
+--------------------+
| + __init__()       |
+--------------------+

+--------------------+
|   ParkingSpot      |
+--------------------+
| - spot_id          |
| - is_available     |
| - vehicle          |
+--------------------+
| + __init__()       |
| + park_vehicle()   |
| + remove_vehicle() |
+--------------------+

+--------------------+
|    ParkingLot      |
+--------------------+
| - spots            |
+--------------------+
| + __init__()       |
| + add_parking_spot()|
| + park_vehicle()   |
| + remove_vehicle() |
| + get_available_spots() |
+--------------------+


"""


class Vehicle:
    def __init__(self, license_plate):
        self.license_plate = license_plate


class Car(Vehicle):
    def __init__(self, license_plate, make, model):
        super().__init__(license_plate)
        self.make = make
        self.model = model


class ParkingSpot:
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.is_available = True
        self.vehicle = None


#     def park_vehicle(self, vehicle):
#         if self.is_available:
#             self.vehicle = vehicle
#             self.is_available = False
#         else:
#             raise Exception(f"Spot {self.spot_id} is already occupied.")

#     def remove_vehicle(self):
#         if not self.is_available:
#             self.vehicle = None
#             self.is_available = True
#         else:
#             raise Exception(f"Spot {self.spot_id} is already empty.")


# class ParkingLot:
#     def __init__(self):
#         self.spots = {}

#     def add_parking_spot(self, spot_id):
#         if spot_id not in self.spots:
#             self.spots[spot_id] = ParkingSpot(spot_id)
#         else:
#             raise Exception(f"Spot {spot_id} already exists.")

#     def park_vehicle(self, spot_id, vehicle):
#         if spot_id in self.spots:
#             self.spots[spot_id].park_vehicle(vehicle)
#         else:
#             raise Exception(f"Spot {spot_id} does not exist.")

#     def remove_vehicle(self, spot_id):
#         if spot_id in self.spots:
#             self.spots[spot_id].remove_vehicle()
#         else:
#             raise Exception(f"Spot {spot_id} does not exist.")

#     def get_available_spots(self):
#         return [spot_id for spot_id, spot in self.spots.items() if spot.is_available]


# # Example usage
# parking_lot = ParkingLot()
# parking_lot.add_parking_spot("A1")
# parking_lot.add_parking_spot("A2")

# car1 = Car("ABC123", "Toyota", "Corolla")
# car2 = Car("XYZ789", "Honda", "Civic")

# parking_lot.park_vehicle("A1", car1)
# parking_lot.park_vehicle("A2", car2)

# print("Available spots:", parking_lot.get_available_spots())

# parking_lot.remove_vehicle("A1")
# parking_lot.remove_vehicle("A2")

# print("Available spots:", parking_lot.get_available_spots())
