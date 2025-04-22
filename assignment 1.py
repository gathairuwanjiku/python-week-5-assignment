# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Subclass: Train
class Train(Vehicle):
    def move(self):
        print("Chugging along the tracks 🚂")

# List of different vehicles
vehicles = [Car(), Plane(), Boat(), Train()]

# Demonstrate polymorphism
for v in vehicles:
    v.move()