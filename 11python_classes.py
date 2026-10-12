#!/usr/bin/env python3
# Unit 11: Model related data and behavior with a class and its objects.
#
# Big idea: a class is a blueprint; an object (instance) is one thing built
# from that blueprint. Attributes store an object's data and methods are
# functions that belong to the object.


# --- 1. A first class ------------------------------------------------------------------
## class creates a new blueprint called Pet. Class names use CapitalWords.
class Pet:
    """A simple example class describing a pet."""

    ## __init__ runs automatically when a new Pet object is created.
    def __init__(self, name, species):
        ## self is the new object; self.name stores data ON that object.
        self.name = name
        ## Another attribute for this object.
        self.species = species

    ## A method is a function defined inside a class.
    def introduce(self):
        ## Methods use self to read this particular object's data.
        return f"{self.name} is a {self.species}."


## Calling the class like a function creates an instance (object).
my_pet = Pet("Mochi", "cat")
## Call the method on the object with a dot.
print(my_pet.introduce())
## A second, separate object built from the same blueprint.
other_pet = Pet("Bao", "dog")
## Each object keeps its own data.
print(other_pet.introduce())
## Attributes can be read directly with a dot too.
print("Attribute access:", my_pet.name, "and", other_pet.name)


# --- 2. Methods that change state ---------------------------------------------------------
## A class that keeps track of money.
class BankAccount:
    """Track a balance with deposits and withdrawals."""

    ## A class attribute is shared by every account.
    interest_rate = 0.02

    ## balance=0 gives new accounts a default balance.
    def __init__(self, owner, balance=0):
        ## Instance attributes: each account has its own copy.
        self.owner = owner
        ## The current amount of money.
        self.balance = balance
        ## A list to remember every transaction.
        self.history = []

    ## Add money to the account.
    def deposit(self, amount):
        ## Refuse zero or negative deposits.
        if amount <= 0:
            ## Stop with a clear error (Unit 10).
            raise ValueError("deposit must be positive")
        ## Increase the balance.
        self.balance += amount
        ## Record the transaction as a tuple.
        self.history.append(("deposit", amount))

    ## Take money out if there is enough.
    def withdraw(self, amount):
        ## Not enough money?
        if amount > self.balance:
            ## Explain and refuse.
            print(f"  Sorry {self.owner}, not enough money.")
            ## False tells the caller it failed.
            return False
        ## Reduce the balance.
        self.balance -= amount
        ## Record it.
        self.history.append(("withdraw", amount))
        ## True tells the caller it worked.
        return True

    ## Add interest using the shared class attribute.
    def add_interest(self):
        ## self.interest_rate finds the class attribute through the object.
        self.balance += self.balance * self.interest_rate

    ## __str__ controls what print(object) shows.
    def __str__(self):
        ## :,.2f adds thousands separators and two decimals.
        return f"{self.owner}'s account: {self.balance:,.2f} baht"


## Open an account with 1000 baht.
account = BankAccount("Nok", 1000)
## Balance becomes 1500.
account.deposit(500)
## Refused: 2000 is more than 1500.
account.withdraw(2000)
## Balance becomes 1200.
account.withdraw(300)
## 2% interest: 1200 * 1.02 = 1224.
account.add_interest()
## print() uses __str__.
print(account)
## The list of recorded transactions.
print("History:", account.history)


# --- 3. Other special ("dunder") methods -------------------------------------------------------
## Double-underscore methods let objects work with normal Python syntax.
class Vector:
    ## Store the two parts of a 2-D vector.
    def __init__(self, x, y):
        ## The horizontal part.
        self.x = x
        ## The vertical part.
        self.y = y

    ## __add__ runs when we write v1 + v2.
    def __add__(self, other):
        ## Return a NEW vector made by adding the matching parts.
        return Vector(self.x + other.x, self.y + other.y)

    ## __eq__ runs when we write v1 == v2.
    def __eq__(self, other):
        ## Equal when both parts match.
        return self.x == other.x and self.y == other.y

    ## __repr__ gives a developer-friendly description.
    def __repr__(self):
        ## Looks like the code that would create this vector.
        return f"Vector({self.x}, {self.y})"


## Uses __add__, then __repr__ to display: Vector(4, 6).
print(Vector(1, 2) + Vector(3, 4))
## Uses __eq__: True.
print("Equal?", Vector(1, 1) == Vector(1, 1))


# --- 4. Properties: computed or protected attributes -----------------------------------------------
## A leading underscore (_celsius) means "internal, use the property instead".
class Thermometer:
    ## Store the starting temperature.
    def __init__(self, celsius):
        ## This assignment goes through the setter below, so it is checked.
        self.celsius = celsius

    ## @property makes a method readable like an attribute: thermo.celsius
    @property
    def celsius(self):
        ## Give back the stored value.
        return self._celsius

    ## The setter runs on thermo.celsius = value.
    @celsius.setter
    def celsius(self, value):
        ## Nothing can be colder than absolute zero.
        if value < -273.15:
            ## Refuse the value.
            raise ValueError("below absolute zero!")
        ## Store the checked value.
        self._celsius = value

    ## A read-only property calculated each time it is read.
    @property
    def fahrenheit(self):
        ## Convert using the formula from Unit 6.
        return self._celsius * 9 / 5 + 32


## Create a thermometer reading 30°C.
thermo = Thermometer(30)
## Read both properties: 30°C is 86.0°F.
print(f"{thermo.celsius}°C is {thermo.fahrenheit}°F")
## Try to set an impossible value.
try:
    ## The setter raises ValueError.
    thermo.celsius = -500
## Catch it.
except ValueError as error:
    ## Show the message.
    print("Rejected:", error)


# --- 5. Objects working together ---------------------------------------------------------------------
## A Shelter "has" many Pet objects (this is called composition).
class Shelter:
    ## Start with no pets.
    def __init__(self):
        ## An empty list to hold Pet objects.
        self.pets = []

    ## Add one pet.
    def admit(self, pet):
        ## Store the Pet object in the list.
        self.pets.append(pet)

    ## __len__ lets us write len(shelter).
    def __len__(self):
        ## The number of pets in the list.
        return len(self.pets)

    ## Print every pet.
    def report(self):
        ## Visit each Pet object.
        for pet in self.pets:
            ## Each pet introduces itself using its own method.
            print("  -", pet.introduce())


## Create an empty shelter.
shelter = Shelter()
## Admit the first pet.
shelter.admit(my_pet)
## Admit the second pet.
shelter.admit(other_pet)
## A heading.
print("Shelter residents:")
## Ask the shelter to list its pets.
shelter.report()
## len() works because we defined __len__.
print("Number of residents:", len(shelter))

## Inheritance (one class building on another) continues in Unit 12.

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Add a birthday() method to Pet that increases an age attribute.
#   2. Create a Rectangle class with area() and perimeter() methods.
#   3. Give BankAccount a transfer(other_account, amount) method.
#   4. Add a find(name) method to Shelter that returns the matching Pet.
# ---------------------------------------------------------------------------
