"""String Insertion."""

print('I have inserted {}.'.format('INSERT'))
print('The animals are {0}, {1}, and {2}.'.format('fox', 'hound', 'bird'))
print('The animals are {0}, {0}, and {0}.'.format('fox', 'hound', 'bird'))
print('The animals are {f}, {h}, and {b}.'.format(f='fox', h='hound',
                                                  b='bird'))

result = 100.0 / 777.0
print('Result = {}'.format(result))
print('Result = {r}'.format(r=result))
print('Result = {r:1.3f}'.format(r=result))
print('Result = {r:10.3f}'.format(r=result))
print('Result = {r:10.6f}'.format(r=result))

name = 'Carol'
print(f'Her name is {name}')
