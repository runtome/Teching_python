#!/usr/bin/env python3
# Unit 12: Build new classes from existing ones with inheritance.
#
# Big idea: a "child" class inherits the attributes and methods of a "parent"
# class, then adds or changes (overrides) only what is different. This avoids
# copying the same code into many classes.


# --- 1. A parent class ------------------------------------------------------------------
class Animal:
    """Behaviour shared by every animal."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def describe(self):
        # self.speak() calls the child's version if the child overrides it.
        return f"{self.name} says {self.speak()}"


# --- 2. Child classes ------------------------------------------------------------------------
# class Child(Parent): means "Child is a kind of Parent".
class Dog(Animal):
    def speak(self):                 # override the parent's method
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Fish(Animal):
    pass                             # inherits everything unchanged


for animal in [Dog("Bao"), Cat("Mochi"), Fish("Nemo")]:
    print(animal.describe())


# --- 3. Extending __init__ with super() ---------------------------------------------------------
# super() calls the parent's version so we don't repeat its work.
class GuideDog(Dog):
    def __init__(self, name, owner):
        super().__init__(name)       # let Animal set self.name
        self.owner = owner           # then add what is new

    def describe(self):
        # Reuse the parent's text and add to it.
        return super().describe() + f" (guides {self.owner})"


guide = GuideDog("Lucky", "Somchai")
print(guide.describe())


# --- 4. Checking relationships -------------------------------------------------------------------
print("Is guide a Dog?", isinstance(guide, Dog))
print("Is guide an Animal?", isinstance(guide, Animal))
print("Is guide a Cat?", isinstance(guide, Cat))
print("Is GuideDog a subclass of Animal?", issubclass(GuideDog, Animal))


# --- 5. Polymorphism: same call, different behaviour -------------------------------------------------
# Code that works with the parent works with every child automatically.
class Shape:
    def area(self):
        raise NotImplementedError("each shape must define area()")

    def __str__(self):
        return f"{type(self).__name__} with area {self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    # A square is a rectangle whose sides are equal.
    def __init__(self, side):
        super().__init__(side, side)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


shapes = [Rectangle(2, 5), Square(3), Circle(1)]
for shape in shapes:
    print(shape)
print("Total area:", round(sum(shape.area() for shape in shapes), 2))


# --- 6. Composition vs inheritance ------------------------------------------------------------------
# Use inheritance for "is a" (a Dog IS an Animal).
# Use composition for "has a" (a Car HAS an Engine): store an object inside.
class Engine:
    def start(self):
        return "Engine running"


class Car:
    def __init__(self):
        self.engine = Engine()       # composition

    def drive(self):
        return self.engine.start() + ", car moving."


print(Car().drive())

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Add a Bird class whose speak() returns "Tweet!" and add a fly() method.
#   2. Create a Triangle(Shape) class using area = base * height / 2.
#   3. Make a SavingsAccount that inherits from a BankAccount (Unit 11) and
#      refuses withdrawals that would leave less than 100 baht.
# ---------------------------------------------------------------------------
