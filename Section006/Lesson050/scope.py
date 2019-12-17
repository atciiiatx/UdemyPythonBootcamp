"""Scope experiments."""

x = 50


def print_func(x):
    """Print."""
    print(f'x = {x}')
    x = 200
    print(f'New x = {x}')


print_func(x)
print_func(x)


y = 2


def print_func2():
    """Print."""
    global y
    print(f'y = {y}')
    y = 200
    print(f'New y = {y}')


print_func2()
print_func2()
