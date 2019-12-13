"""Args Experiments."""


def calculate_tip(*args):
    """Calculate a tip."""
    print(f'args = {args}')
    return sum(args) * 0.15


def check_fruit(**kwargs):
    """Check for fruit."""
    if 'fruit' in kwargs:
        print(f'Fruit in {kwargs} is {kwargs["fruit"]}')
    else:
        print(f'No fruit in {kwargs}')


print(f'tip = {calculate_tip(1.0)}')
print(f'tip = {calculate_tip(1.0, 3.5, 11.25)}')

check_fruit(fruit='apple')
check_fruit(fruit='pear')
check_fruit(ball='baseball')
