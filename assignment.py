# Base class
class Superhero:
    def _init_(self, name, power, health):
        self.name = name
        self._power = power      # Encapsulated attribute (protected)
        self.health = health

    def display_info(self):
        return f"{self.name} has {self._power} power and {self.health} health."

    def use_power(self):
        return f"{self.name} uses {self._power}!"

# Subclass 1
class FlyingHero(Superhero):
    def _init_(self, name, health, flight_speed):
        super()._init_(name, "Flight", health)
        self.flight_speed = flight_speed

    def use_power(self):
        return f"{self.name} soars through the sky at {self.flight_speed} mph!"

# Subclass 2
class StrongHero(Superhero):
    def _init_(self, name, health, strength_level):
        super()._init_(name, "Super Strength", health)
        self.strength_level = strength_level

    def use_power(self):
        return f"{self.name} lifts a car with strength level {self.strength_level}!"

# Subclass 3
class TechHero(Superhero):
    def _init_(self, name, health, gadget):
        super()._init_(name, "Tech", health)
        self.gadget = gadget

    def use_power(self):
        return f"{self.name} uses their high-tech {self.gadget} to save the day!"

# Example usage
heroes = [
    FlyingHero("SkyWing", 100, 300),
    StrongHero("BulkMaster", 120, 95),
    TechHero("GizmoGirl", 90, "Cyber Drone")
]

for hero in heroes:
    print(hero.display_info())
    print(hero.use_power())
    print()