"""Error/exception homework."""


# Problem 1
# Handle the exception thrown by the code below by using try and except blocks.
print('\nProblem 1')
for i in ['a', 'b', 'c']:
    try:
        print(i**2)
    except TypeError:
        print(f'Type error computing the square of {i}')
    except:
        print(f'Trouble computing the square of {i}')

# Problem 2
# Handle the exception thrown by the code below by using try and except blocks.
# Then use a finally block to print 'All Done.'

print('\nProblem 2')
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print('Zero Division Error')
finally:
    print('All Done.')

# Problem 3
# Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try, except, else block to account for
# incorrect inputs.


def ask():
    """Ask for an integer and return its square."""
    while True:
        try:
            num = int(input('Please input a number:'))
        except:
            print('Tha is not a number. Please try again.')
        else:
            break
    print(f'Your number is {num}')
    print(f'Square = {num * num}')


print('\nProblem 3')
sq = ask()
