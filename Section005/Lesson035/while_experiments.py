"""While experiments."""

x = 0
while x < 5:
    print(f'x = {x}')
    x += 1

xlist = [1, 2, 3]
for item in xlist:
    pass

mystring = 'Sammy Sosa'
for letter in mystring:
    if (letter == 'a'):
        continue
    print(letter)

for letter in mystring:
    if (letter == 'y'):
        break
    print(letter)
