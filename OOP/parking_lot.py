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

    def park_vehicle(self, vehicle):
        if self.is_available:
            self.is_available = False
            self.vehicle = vehicle
        else:
            raise Exception(f"Spot {self.spot_id} is already occupied.")

    def remove_vehicle(self, vehicle):
        if self.is_available == False:
            self.is_available = True
            self.vehicle = None
        else:
            raise Exception(f"Spot {self.spot_id} is already empty.")


class ParkingLot:
    def __init__(self) -> None:
        self.spots = {}

    def add_parking_spot(self, parking_spot):
        if parking_spot.spot_id not in self.spots:
            self.spots[parking_spot.spot_id] = ParkingSpot(parking_spot.spot_id)
        else:
            raise Exception(f"Spot {parking_spot.spot_id} already exists.")

    def park_vehicle(self, spot_id, vehicle):
        if spot_id in self.spots:
            self.spots[spot_id].park_vehicle(vehicle)
        else:
            raise Exception(f"Spot {spot_id} does not exist. Need to create spot id.")

    def remove_vehicle(self, spot_id):
        if spot_id in self.spots:
            self.spots[spot_id].remove_vehicle()
        else:
            raise Exception(f"Spot {spot_id} does not exist.")

    def get_available_spots(self):

        available = [
            spot_id for spot_id, spot in self.spots.items() if spot.vehicle is None
        ]

        print(available)
        return available


p_spot1 = ParkingSpot("A1")
p_spot2 = ParkingSpot("A2")

p_lot = ParkingLot()
p_lot.add_parking_spot(p_spot1)
p_lot.add_parking_spot(p_spot2)

car1 = Car("ATT891", "Tesla", "2024")
p_lot.get_available_spots()
p_lot.park_vehicle("A1", car1)
p_lot.get_available_spots()
