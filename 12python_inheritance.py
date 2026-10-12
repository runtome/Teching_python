#!/usr/bin/env python3
# Unit 12: Build new classes from existing ones with inheritance.
#
# Big idea: a "child" class inherits the attributes and methods of a "parent"
# class, then adds or changes (overrides) only what is different. This avoids
# copying the same code into many classes.


# --- 1. A parent class ------------------------------------------------------------------
## The parent class holds behaviour every animal shares.
class Animal:
    """Behaviour shared by every animal."""

    ## Every animal has a name.
    def __init__(self, name):
        ## Store the name on the object.
        self.name = name

    ## A default sound that child classes can replace.
    def speak(self):
        ## A generic animal makes no particular sound.
        return "..."

    ## Shared method that uses speak().
    def describe(self):
        ## self.speak() calls the CHILD's version if the child overrides it.
        return f"{self.name} says {self.speak()}"


# --- 2. Child classes ------------------------------------------------------------------------
## class Dog(Animal): means "a Dog is a kind of Animal".
class Dog(Animal):
    ## Defining speak() again overrides the parent's version.
    def speak(self):
        ## The dog's own sound.
        return "Woof!"


## Another child class.
class Cat(Animal):
    ## Override speak() for cats.
    def speak(self):
        ## The cat's own sound.
        return "Meow!"


## A child with no changes at all.
class Fish(Animal):
    ## pass means "nothing to add": Fish inherits everything unchanged.
    pass


## Make one of each and loop over them.
for animal in [Dog("Bao"), Cat("Mochi"), Fish("Nemo")]:
    ## Same method call, different result for each class.
    print(animal.describe())


# --- 3. Extending __init__ with super() ---------------------------------------------------------
## GuideDog is a Dog, which is an Animal.
class GuideDog(Dog):
    ## A guide dog also needs an owner.
    def __init__(self, name, owner):
        ## super() calls the parent's __init__ so self.name is set there.
        super().__init__(name)
        ## Then add the new attribute.
        self.owner = owner

    ## Extend the parent's describe() rather than replacing it.
    def describe(self):
        ## Reuse the parent's text, then add extra information.
        return super().describe() + f" (guides {self.owner})"


## Create a guide dog.
guide = GuideDog("Lucky", "Somchai")
## Shows "Lucky says Woof! (guides Somchai)".
print(guide.describe())


# --- 4. Checking relationships -------------------------------------------------------------------
## isinstance() asks "is this object a kind of that class?" — True.
print("Is guide a Dog?", isinstance(guide, Dog))
## True as well, because a Dog is an Animal.
print("Is guide an Animal?", isinstance(guide, Animal))
## False: GuideDog has nothing to do with Cat.
print("Is guide a Cat?", isinstance(guide, Cat))
## issubclass() asks the same question about classes themselves.
print("Is GuideDog a subclass of Animal?", issubclass(GuideDog, Animal))
## __mro__ shows the order Python searches for methods.
print("Method lookup order:", [cls.__name__ for cls in GuideDog.__mro__])


# --- 5. Polymorphism: same call, different behaviour -------------------------------------------------
## A parent that defines what every shape must be able to do.
class Shape:
    ## Children MUST replace this method.
    def area(self):
        ## Raise an error if a child forgot to define area().
        raise NotImplementedError("each shape must define area()")

    ## Shared __str__ that works for every child.
    def __str__(self):
        ## type(self).__name__ is the child's class name, e.g. "Circle".
        return f"{type(self).__name__} with area {self.area():.2f}"


## A rectangle is a Shape.
class Rectangle(Shape):
    ## Store the sides.
    def __init__(self, width, height):
        ## The width.
        self.width = width
        ## The height.
        self.height = height

    ## The rectangle's own area formula.
    def area(self):
        ## Width times height.
        return self.width * self.height


## A square is a rectangle whose sides are equal.
class Square(Rectangle):
    ## Only one side length is needed.
    def __init__(self, side):
        ## Pass the same value as width and height to Rectangle.
        super().__init__(side, side)


## A circle is a Shape with a different formula.
class Circle(Shape):
    ## Store the radius.
    def __init__(self, radius):
        ## The distance from the centre to the edge.
        self.radius = radius

    ## The circle's own area formula.
    def area(self):
        ## pi times radius squared.
        return 3.14159 * self.radius ** 2


## A mixed list of different shapes.
shapes = [Rectangle(2, 5), Square(3), Circle(1)]
## The same loop works for every shape.
for shape in shapes:
    ## print() calls the shared __str__, which calls each shape's own area().
    print(shape)
## A generator expression (Unit 14) adds up every area.
print("Total area:", round(sum(shape.area() for shape in shapes), 2))


# --- 6. Composition vs inheritance ------------------------------------------------------------------
## Inheritance means "is a" (a Dog IS an Animal).
## Composition means "has a" (a Car HAS an Engine): store an object inside.
class Engine:
    ## What an engine can do.
    def start(self):
        ## Return a status message.
        return "Engine running"


## The car is not an engine, so it does not inherit from Engine.
class Car:
    ## Build the car with an engine inside.
    def __init__(self):
        ## Composition: the car stores an Engine object.
        self.engine = Engine()

    ## Driving uses the engine.
    def drive(self):
        ## Ask the engine to start, then add our own text.
        return self.engine.start() + ", car moving."


## Shows "Engine running, car moving."
print(Car().drive())

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Add a Bird class whose speak() returns "Tweet!" and add a fly() method.
#   2. Create a Triangle(Shape) class using area = base * height / 2.
#   3. Make a SavingsAccount that inherits from a BankAccount (Unit 11) and
#      refuses withdrawals that would leave less than 100 baht.
# ---------------------------------------------------------------------------
