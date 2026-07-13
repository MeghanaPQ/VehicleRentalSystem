from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class RentalReceipt:
    vehicle_id: str
    customer_name: str
    days: int
    total_cost: float


class Vehicle(ABC):
    def __init__(self, vehicle_id: str, brand: str, rate_per_day: float) -> None:
        self._vehicle_id = vehicle_id
        self._brand = brand
        self._rate_per_day = rate_per_day
        self._is_available = True

    @property
    def vehicle_id(self) -> str:
        return self._vehicle_id

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def rate_per_day(self) -> float:
        return self._rate_per_day

    @property
    def is_available(self) -> bool:
        return self._is_available

    def rent(self) -> None:
        self._is_available = False

    def return_vehicle(self) -> None:
        self._is_available = True

    @abstractmethod
    def calculate_rental_cost(self, days: int) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_vehicle_type(self) -> str:
        raise NotImplementedError

    def display_info(self) -> str:
        status = "Available" if self._is_available else "Rented"
        return f"{self.get_vehicle_type()} {self._brand} ({self._vehicle_id}) - ${self._rate_per_day}/day - {status}"


class Car(Vehicle):
    def __init__(self, vehicle_id: str, brand: str, rate_per_day: float, seats: int) -> None:
        super().__init__(vehicle_id, brand, rate_per_day)
        self._seats = seats

    @property
    def seats(self) -> int:
        return self._seats

    def calculate_rental_cost(self, days: int) -> float:
        return self._rate_per_day * days

    def get_vehicle_type(self) -> str:
        return "Car"


class Bike(Vehicle):
    def __init__(self, vehicle_id: str, brand: str, rate_per_day: float, engine_cc: int) -> None:
        super().__init__(vehicle_id, brand, rate_per_day)
        self._engine_cc = engine_cc

    @property
    def engine_cc(self) -> int:
        return self._engine_cc

    def calculate_rental_cost(self, days: int) -> float:
        return self._rate_per_day * days

    def get_vehicle_type(self) -> str:
        return "Bike"


class RentalSystem:
    def __init__(self) -> None:
        self._vehicles: List[Vehicle] = []
        self._rentals: List[RentalReceipt] = []

    def add_vehicle(self, vehicle: Vehicle) -> None:
        self._vehicles.append(vehicle)

    def available_vehicles(self) -> List[Vehicle]:
        return [vehicle for vehicle in self._vehicles if vehicle.is_available]

    def rent_vehicle(self, vehicle_id: str, days: int, customer_name: str) -> RentalReceipt:
        for vehicle in self._vehicles:
            if vehicle.vehicle_id == vehicle_id and vehicle.is_available:
                vehicle.rent()
                total_cost = vehicle.calculate_rental_cost(days)
                receipt = RentalReceipt(vehicle_id=vehicle_id, customer_name=customer_name, days=days, total_cost=total_cost)
                self._rentals.append(receipt)
                return receipt
        raise ValueError("Vehicle is not available for rent")

    def return_vehicle(self, vehicle_id: str) -> None:
        for vehicle in self._vehicles:
            if vehicle.vehicle_id == vehicle_id:
                vehicle.return_vehicle()
                return
        raise ValueError("Vehicle not found")

    def list_inventory(self) -> List[str]:
        return [vehicle.display_info() for vehicle in self._vehicles]


def display_vehicle_summary(vehicle: Vehicle) -> str:
    return vehicle.display_info()


if __name__ == "__main__":
    rental_system = RentalSystem()
    rental_system.add_vehicle(Car("C101", "Toyota", 60, 5))
    rental_system.add_vehicle(Bike("B202", "Honda", 25, 150))

    print("Welcome to the Vehicle Rental System")
    print("Inventory:")
    for item in rental_system.list_inventory():
        print("-", item)

    receipt = rental_system.rent_vehicle("C101", 3, "Ava")
    print(f"\nRental receipt for {receipt.customer_name}: ${receipt.total_cost} for {receipt.days} days")

    rental_system.return_vehicle("C101")
    print("\nVehicle returned. Inventory updated:")
    for item in rental_system.list_inventory():
        print("-", item)
