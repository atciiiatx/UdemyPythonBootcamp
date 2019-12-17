"""Homework for Section 6."""
import math
import string


def vol(rad):
    """Calculate volume of sphere."""
    return (4.0 / 3.0) * math.pi * (rad**3)


test_rads = [x for x in range(1, 5)]
test_vols = list(map(vol, test_rads))
print(f'rads = {test_rads} vols = {test_vols}')


def ran_check(num, low, high):
    """Check if number in range. Print result."""
    in_range = num in range(low, high)
    print(f'{num} in range ({low}, {high} : {in_range})')


def ran_bool(num, low, high):
    """Boolean check if number in range."""
    return num in range(low, high)


test_nums = [x for x in range(-3, 4)]
lo = -1
hi = 2
for num in test_nums:
    ran_check(num, lo, hi)

range_checks = list(map(lambda x: ran_bool(x, lo, hi), test_nums))
print(f'nums: {test_nums} range_checks: {range_checks}')


def up_low(s):
    """Count upper and lower case strings."""
    high_count = 0
    low_count = 0
    for c in s:
        if c.isupper():
            high_count += 1
        elif c.islower():
            low_count += 1
    return [high_count, low_count]


sample_str = 'Hello Mr. Rogers, how are you this fine Tuesday?'
sample_counts = up_low(sample_str)
print(f'Uppercase: {sample_counts[0]} Lowercase: {sample_counts[1]}')


def unique_list(l):
    """Find unique elements of a list."""
    result = []
    for x in l:
        if not (x in result):
            result.append(x)
    return result


test_list = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 5]
print(f'Uniques from {test_list} = {unique_list(test_list)}')


def multiply(numbers):
    """Multiply."""
    product = 1
    for n in numbers:
        product *= n
    return product


mult_nums = [1, 2, 3, -4]
print(f'multiply {mult_nums} = {multiply(mult_nums)}')


def palindrome(s):
    """Check for palindrome."""
    lo = 0
    hi = len(s) - 1
    while (lo <= hi):
        if (s[lo] != s[hi]):
            return False
        lo += 1
        hi -= 1
    return True


pal_data = ['helleh', 'hello', 'bob']
pal_result = list(map(palindrome, pal_data))
print(f'Palindrome test for {pal_data} = {pal_result}')


def ispangram(s, alphabet=string.ascii_lowercase):
    """Determine if a string contains all letters."""
    slower = s.lower()
    for a in alphabet:
        if not (a in slower):
            return False
    return True


test_pans = ['The quick brown fox jumps over the lazy dog', 'hello']
for p in test_pans:
    print(f'{p} is pangram: {ispangram(p)}')
