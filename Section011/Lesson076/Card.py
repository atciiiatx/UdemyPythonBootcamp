"""Card class."""

import random


class Card:
    """Playing card."""

    # Constants
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = (
        'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
        'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {
        'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
        'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
        'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self, suit, rank):
        """Constructor."""
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Convert to string."""
        return self.rank + ' of ' + self.suit

    def value(self):
        """Numerical value of card."""
        return Card.values[self.rank]


if __name__ == '__main__':
    print('CARD UNIT TEST')
    for i in range(0, 10):
        s = random.choice(Card.suits)
        r = random.choice(Card.ranks)
        card = Card(s, r)
        print(f'Card: {card} Value: {card.value()}')
