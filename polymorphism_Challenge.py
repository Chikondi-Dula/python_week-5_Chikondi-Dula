# Base Class: Vehicle
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        pass  # Will be overridden in subclasses

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving on the road 🚗")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying in the sky ✈️")
2
# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing on water ⛵")

# Polymorphism in action
vehicles = [
    Car("Toyota"),
    Plane("Boeing 747"),
    Boat("Titanic")
]

# Each vehicle has the same method name but behaves differently
for vehicle in vehicles:
    vehicle.move()
