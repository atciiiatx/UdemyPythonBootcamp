"""Polymorphism experiments."""


class Animal():
    """Animal."""

    def __init__(self, name):
        """Constructor."""
        self.name = name

    def speak(self):
        """Emit sound."""
        raise NotImplementedError('Derived class must implement speak.')


class Dog(Animal):
    """Dog."""

    def speak(self):
        """Emit sound."""
        print(f'{self.name} says Woof!')


class Cat(Animal):
    """Cat."""

    def speak(self):
        """Emit sound."""
        print(f'{self.name} says Meow!')


pets = [Dog('Fido'), Cat('Felix')]
for pet in pets:
    pet.speak()
