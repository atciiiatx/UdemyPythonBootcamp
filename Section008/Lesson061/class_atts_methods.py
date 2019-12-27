"""Class attributed experiments."""


class Dog():
    """ Dog class."""

    # Class object attributes
    species = 'Mammal'

    def __init__(self, breed, name, spots=False):
        """Constructor."""
        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self):
        """Make dog sound."""
        print(f"WOOF! My name is {self.name}")


pet = Dog('Collie', 'Lassie')
print(f'pet = {pet.species} {pet.breed} {pet.name}')
pet.bark()
