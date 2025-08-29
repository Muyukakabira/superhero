# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclasses with their own versions of move()
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")

# Function that demonstrates polymorphism
def travel(vehicle):
    vehicle.move()

# Create instances
vehicles = [Car(), Plane(), Boat(), Bicycle()]

# Let each vehicle move
for v in vehicles:
    travel(v)