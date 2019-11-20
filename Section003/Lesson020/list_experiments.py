"""List experiments."""

list1 = ['one', 'two', 'three']
list2 = ['four', 'five', 'six']
full_list = list1 + list2
print(f'full_list = {full_list}')

full_list[0] = 'ONE'
print(f'full_list = {full_list}')

full_list.append('SEVEN')
print(f'full_list = {full_list}')

last = full_list.pop()
print(f'last = {last}')
print(f'full_list = {full_list}')

first = full_list.pop(0)
print(f'first = {first}')
print(f'full_list = {full_list}')

letter_list = ['z', 'a', 'f', 'y', 't', 's', 'm', 'p', 'q']
print(f'latter_list = {letter_list}')
letter_list.sort()
print(f'sorted_list = {letter_list}')

letter_list.reverse()
print(f'reverse_list = {letter_list}')

print(f'full_list = {full_list}')
full_list.reverse()
print(f'reverse_full_list = {full_list}')