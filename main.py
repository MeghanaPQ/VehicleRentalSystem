from vehicle_rental import Bike, Car, RentalSystem


def main() -> None:
    system = RentalSystem()
    system.add_vehicle(Car("C101", "Toyota", 60, 5))
    system.add_vehicle(Bike("B202", "Honda", 25, 150))

    print("Vehicle Rental System Demo")
    print("Available vehicles:")
    for vehicle in system.available_vehicles():
        print(f"- {vehicle.display_info()}")

    receipt = system.rent_vehicle("C101", 3, "Ava")
    print(f"\nReceipt: {receipt.customer_name} rented C101 for {receipt.days} days")
    print(f"Total cost: ${receipt.total_cost}")

    system.return_vehicle("C101")
    print("\nVehicle returned successfully.")


if __name__ == "__main__":
    main()
