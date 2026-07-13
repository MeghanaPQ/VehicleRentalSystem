# Vehicle Rental System

A simple Python project that demonstrates Object-Oriented Programming (OOP) through a vehicle rental system.

## Project Overview
This project models a basic vehicle rental system where users can:
- add vehicles to the system
- rent available vehicles
- return rented vehicles
- view the current inventory

It uses OOP concepts such as:
- Classes and Objects
- Encapsulation
- Abstraction
- Functions and Methods

## Features
- Base class for all vehicles
- Specialized classes for Car and Bike
- Rental management through a RentalSystem class
- Receipt generation for rentals
- Console-based demo output

## Project Files
- `vehicle_rental.py` - Main OOP implementation
- `main.py` - Demo program to run the system
- `test_vehicle_rental.py` - Unit tests for core functionality

## Requirements
- Python 3.x

## How to Run
1. Open the project folder
2. Run the following command:

```bash
python main.py
```

## How to Run Tests
Run the following command:

```bash
python -m unittest -v
```

## Example Output
```text
Vehicle Rental System Demo
Available vehicles:
- Car Toyota (C101) - $60/day - Available
- Bike Honda (B202) - $25/day - Available

Receipt: Ava rented C101 for 3 days
Total cost: $180

Vehicle returned successfully.
```
