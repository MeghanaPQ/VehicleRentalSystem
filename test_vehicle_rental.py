import unittest
from vehicle_rental import Car, Bike, RentalSystem


class VehicleRentalSystemTests(unittest.TestCase):
    def setUp(self):
        self.system = RentalSystem()
        self.car = Car("C101", "Toyota", 60, 5)
        self.bike = Bike("B202", "Honda", 25, 150)
        self.system.add_vehicle(self.car)
        self.system.add_vehicle(self.bike)

    def test_vehicle_is_added_to_inventory(self):
        self.assertEqual(len(self.system.available_vehicles()), 2)

    def test_renting_vehicle_marks_it_unavailable(self):
        receipt = self.system.rent_vehicle("C101", 3, "Ava")
        self.assertEqual(receipt.customer_name, "Ava")
        self.assertEqual(receipt.total_cost, 180)
        self.assertEqual(len(self.system.available_vehicles()), 1)

    def test_returning_vehicle_makes_it_available_again(self):
        self.system.rent_vehicle("B202", 2, "Ben")
        self.system.return_vehicle("B202")
        self.assertEqual(len(self.system.available_vehicles()), 2)


if __name__ == "__main__":
    unittest.main()
