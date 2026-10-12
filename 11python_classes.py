#!/usr/bin/env python3
# Unit 11: Model related data and behavior with a class and its objects.
#
# Big idea: a class is a blueprint; an object (instance) is one thing built
# from that blueprint. Attributes store an object's data and methods are
# functions that belong to the object.


# --- 1. A first class ------------------------------------------------------------------
class Pet:
    """A simple example class describing a pet."""

    def __init__(self, name, species):
        # __init__ runs when a new Pet object is created.
        self.name = name
        self.species = species

    def introduce(self):
        # Methods use self to read data belonging to this particular object.
        return f"{self.name} is a {self.species}."


# Create an instance (object) by calling the class like a function.
my_pet = Pet("Mochi", "cat")
print(my_pet.introduce())

# Each object keeps its own data.
other_pet = Pet("Bao", "dog")
print(other_pet.introduce())
print("Attribute access:", my_pet.name, "and", other_pet.name)


# --- 2. Methods that change state ---------------------------------------------------------
class BankAccount:
    """Track a balance with deposits and withdrawals."""

    interest_rate = 0.02    # class attribute: shared by every account

    def __init__(self, owner, balance=0):
        self.owner = owner          # instance attributes: one per account
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"  Sorry {self.owner}, not enough money.")
            return False
        self.balance -= amount
        self.history.append(("withdraw", amount))
        return True

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

    # __str__ controls what print(object) shows.
    def __str__(self):
        return f"{self.owner}'s account: {self.balance:,.2f} baht"


account = BankAccount("Nok", 1000)
account.deposit(500)
account.withdraw(2000)          # refused
account.withdraw(300)
account.add_interest()
print(account)
print("History:", account.history)


# --- 3. Other special ("dunder") methods -------------------------------------------------------
# Methods with double underscores let your objects work with Python syntax.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):           # lets us write v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):            # lets us write v1 == v2
        return self.x == other.x and self.y == other.y

    def __repr__(self):                 # a developer-friendly description
        return f"Vector({self.x}, {self.y})"


print(Vector(1, 2) + Vector(3, 4))
print("Equal?", Vector(1, 1) == Vector(1, 1))


# --- 4. Properties: computed or protected attributes -----------------------------------------------
# A leading underscore (_celsius) is a convention meaning "internal, please
# use the property instead".
class Thermometer:
    def __init__(self, celsius):
        self.celsius = celsius          # goes through the setter below

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):               # read-only, calculated on demand
        return self._celsius * 9 / 5 + 32


thermo = Thermometer(30)
print(f"{thermo.celsius}°C is {thermo.fahrenheit}°F")
try:
    thermo.celsius = -500
except ValueError as error:
    print("Rejected:", error)


# --- 5. Objects working together ---------------------------------------------------------------------
# One object can hold others: a Shelter "has" many Pet objects.
class Shelter:
    def __init__(self):
        self.pets = []

    def admit(self, pet):
        self.pets.append(pet)

    def report(self):
        for pet in self.pets:
            print("  -", pet.introduce())


shelter = Shelter()
shelter.admit(my_pet)
shelter.admit(other_pet)
print("Shelter residents:")
shelter.report()

# Inheritance (one class building on another) continues in Unit 12.

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Add a birthday() method to Pet that increases an age attribute.
#   2. Create a Rectangle class with area() and perimeter() methods.
#   3. Give BankAccount a transfer(other_account, amount) method.
#   4. Add __len__ to Shelter so len(shelter) returns the number of pets.
# ---------------------------------------------------------------------------
