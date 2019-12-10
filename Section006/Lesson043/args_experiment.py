"""Args Experiments."""

def calculate_tip(*args):
    return sum(args) * 0.15


print(f'tip = {calculate_tip(1.0)}')
print(f'tip = {calculate_tip(1.0, 3.5, 11.25)}')