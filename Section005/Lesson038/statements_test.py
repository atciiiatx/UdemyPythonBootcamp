"""Statements Test."""

# Words that start with 's'
st = 'Print only the words that start with s in this sentence'
for word in st.split(' '):
    if word[0] == 's':
        print(f'starts with s: {word}')

# Even numbers through 10
for i in range(0, 11, 2):
    print(f'even: {i}')

# Numbers divisible by 3
div3 = [x for x in range(1, 51) if x % 3 == 0]
print(f'divisible by 3: {div3}')

# words wiht even lengths
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split(' '):
    if len(word) % 2 == 0:
        print(f'even: {word}')

# Fizz Buzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# First letters
st = 'Create a list of the first letters of every word in this string'
first_letters = [w[0] for w in st.split(' ')]
print(f'first letters = {first_letters}')
