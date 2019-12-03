"""List comprehensions experiments."""

# Naive
my_string = 'hello'
my_list1 = []
for letter in my_string:
    my_list1.append(letter)
print(f'my_list1 = {my_list1}')

my_list2 = [letter for letter in my_string]
print(f'my_list2 = {my_list2}')

my_list3 = [x for x in 'word']
print(f'my_list3 = {my_list3}')

my_list4 = [x for x in range(0, 15)]
print(f'my_list4 = {my_list4}')

my_list5 = [x for x in range(0, 20) if x % 2 == 0]
print(f'my_list5 = {my_list5}')

my_list6 = [x if x % 2 == 0 else 'ODD' for x in range(0, 20)]
print(f'my_list6 = {my_list6}')
