# Base class: Superhero
class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self.__level = level  # Encapsulated attribute

    def introduce(self):
        return f"I am {self.name}, and my power is {self.power}!"

    def get_level(self):
        return self.__level

    def level_up(self):
        self.__level += 1
        return f"{self.name} leveled up to {self.__level}!"

    def attack(self):
        return f"{self.name} attacks with {self.power}!"

# Subclass: FlyingHero (inherits from Superhero)
class FlyingHero(Superhero):
    def __init__(self, name, power, level, flight_speed):
        super().__init__(name, power, level)
        self.flight_speed = flight_speed

    # Polymorphism: override attack method
    def attack(self):
        return f"{self.name} swoops in at {self.flight_speed} km/h and strikes with {self.power}!"

    def fly(self):
        return f"{self.name} is flying at {self.flight_speed} km/h!"

# Create objects
hero1 = Superhero("BoltMan", "Electric Shock", 5)
hero2 = FlyingHero("SkyQueen", "Wind Blast", 7, 300)

# Use methods
print(hero1.introduce())
print(hero1.attack())
print(hero1.level_up())

print(hero2.introduce())
print(hero2.attack())  # Polymorphic behavior
print(hero2.fly())
print(hero2.get_level())  # Encapsulated access