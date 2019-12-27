
"""Object Oriented Programming Challenge.

For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to
make sure the account can't be overdrawn.
"""


class Account:
    """Bank Account."""

    def __init__(self, name, amount):
        """Constructor."""
        self.owner = name
        self.balance = amount

    def __str__(self):
        """Convert to string."""
        return "Acct Owner:\t" + self.owner + "\n" + \
            "Acct Balance:\t$" + str(self.balance)

    def deposit(self, num):
        """Add money."""
        if num < 0:
            print('Can not deposit a negative sum.')
        else:
            self.balance += num
            print(f'Deposit accepted. New balance = ${self.balance}')

    def withdraw(self, num):
        """Remove money."""
        if num < 0:
            print('Can not withdraw a negative sum.')
        elif num > self.balance:
            print('Funds unavailable.')
        else:
            self.balance -= num
            print(f'Withdrawal accepted. New balance = ${self.balance}')


# Instantiate the class
acct1 = Account('Jose', 100)

# Print the object
print(acct1)

# Show the account owner attribute
print(f'owner = {acct1.owner}')

# Show the account balance attribute
print(f'balance = {acct1.balance}')

# Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.withdraw(75)

# Make a withdrawal that exceeds the available balance
acct1.withdraw(500)
