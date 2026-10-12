#!/usr/bin/env python3
# Unit 11: Model related data and behavior with a class and its objects.


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
