"""Function Practice."""
# Warmup


def lesser_of_two_evens(a, b):
    """Return min if both even, max otherwise."""
    if (a % 2 == 0 and b % 2 == 0):
        return min(a, b)
    else:
        return max(a, b)


pairs = [[2, 4], [2, 5]]
for a, b in pairs:
    print(f'lesser_of_two_evens({a},{b}) = {lesser_of_two_evens(a, b)}')


def animal_crackers(text):
    """Check if both words in a string start with same letter."""
    words = text.split()
    return words[0][0].lower() == words[1][0].lower()


animals = ['Levelheaded Llama', 'Crazy Kangaroo']
for a in animals:
    print(f"animal_crackers({a}) = {animal_crackers(a)}")


# Level 1


def old_macdonald(name):
    """Capitalize 1st & 4th letter."""
    result = ''
    for i in range(0, len(name)):
        if i == 0 or i == 3:
            result += name[i].upper()
        else:
            result += name[i]
    return result


name = 'macdonald'
print(f'old_macdonald({name}) = {old_macdonald(name)}')


def master_yoda(text):
    """Reverse words."""
    words = text.split()
    rev = []
    for i in range(1, len(words) + 1):
        rev.append(words[-i])
    return " ".join(rev)


test_strings = ['I am home', 'We are ready']
for s in test_strings:
    print(f'master_yoda({s}) = {master_yoda(s)}')


# Level 2


def has_33(nums):
    """Look for consecutive 3s."""
    last = -1
    for x in nums:
        if last == 3 and x == 3:
            return True
        last = x
    return False


test_data = [[1, 3, 3], [1, 3, 1, 3], [3, 1, 3]]
for td in test_data:
    print(f'has_33({td}) = {has_33(td)}')


# Challenging


def spy_game(nums):
    """Look for 007."""
    has0 = False
    has00 = False
    for x in nums:
        if x == 0:
            if not has0:
                has0 = True
            elif has0:
                has00 = True
        elif x == 7:
            if has00:
                return True
            elif has0:
                has0 = False
    return False


test_lists = [
    [1, 2, 4, 0, 0, 7, 5],
    [1, 0, 2, 4, 0, 5, 7],
    [1, 7, 2, 0, 4, 5, 0]
]
for tl in test_lists:
    print(f'spy_game({tl}) = {spy_game(tl)}')


def count_primes(num):
    """Count primes up to a number."""
    prime_count = 0
    for x in range(2, num + 1):
        is_prime = True
        for y in range(2, x):
            if x % y == 0:
                is_prime = False
        if is_prime:
            prime_count += 1
    return prime_count


test_vals = [10, 25, 100, 200]
for v in test_vals:
    print(f'count_primes({v}) = {count_primes(v)}')
