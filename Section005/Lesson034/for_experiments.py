"""For experiments."""


mylist = (1, 2, 3, 4, 7)
for i in mylist:
    print(i)

list_sum = 0
for i in mylist:
    list_sum += i
    print(f'list_sum = {list_sum}')

mystring = 'Hello World!'
for letter in mystring:
    print(letter)

for _ in mystring:
    print('Cool!')

tuple_list = [(1, 2), (3, 4)]
for a, b in tuple_list:
    print(f'a = {a} b = {b}')

d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d:
    print(f'key = {item}, val = {d[item]}')

for key, val in d.items():
    print(f'key = {key}, val = {val}')
