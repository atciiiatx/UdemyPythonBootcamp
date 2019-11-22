"""Operators Experiments."""

from random import randint, shuffle

for num in range(10):
    print(num)

for num in range(2, 20, 2):
    print(num)

index_count = 0
mystring = 'abcdefghij'
for letter in mystring:
    print(f'Letter for {index_count} is {letter}')
    index_count += 1

for item in enumerate(mystring):
    print(item)

for index, val in enumerate(mystring):
    print(f'Letter for {index} is {val}')

mylistnum = [1, 2, 3, 4, 5, 5, 6, 7, 8]
mylistletter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
for z in zip(mylistnum, mylistletter):
    print(z)

if 3 in mylistnum:
    print('3 is in mylistnum')

if 3 in mylistletter:
    print('3 is in mylistletter')

print(f'min of mylistnume is {min(mylistnum)}')
print(f'max of mylistnume is {max(mylistnum)}')

slist = mylistnum
shuffle(slist)
print(f'shuffled list = {slist}')

r = randint(1, 1000)
print(f'r = {r}')

nstr = input('enter a number:')
nin = int(nstr)
print(f'You typed {nin}')