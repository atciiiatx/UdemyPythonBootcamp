"""Experiments with Lambda expressions, map, and filter."""


def square(num):
    """Compute square of number."""
    return num ** 2


my_nums = [x for x in range(1, 7)]
my_squares = list(map(square, my_nums))
print(f'my_squares = {my_squares}')


def check_even(num):
    """Determine whether even."""
    return num % 2 == 0


my_evens = list(filter(check_even, my_nums))
print(f'my_evens = {my_evens}')

lambda_squares = list(map(lambda x: x ** 2, my_nums))
print(f'lambda_squares = {lambda_squares}')

lambda_evens = list(filter(lambda x: x % 2 == 0, my_nums))
print(f'lambda_evens = {lambda_evens}')

my_names = ['Alice', 'Fred', 'Bruce', 'Kate']
reverses = list(map(lambda s: s[::-1], my_names))
print(f'Reverse of {my_names} = {reverses}')
