"""Class Experiments."""


class Dog():
    """ Dog class."""
    def __init__(self, breed, name, spots=False):
        """Constructor,"""
        self.breed = breed
        self.name = name
        self.spots = spots


my_dog = Dog('Terrier', 'Sammy')
print(f'type of Dog is {type(my_dog)} breed = {my_dog.breed} \
name = {my_dog.name} spots = {my_dog.spots}')
