"""Deck of cards class."""

import random
from Card import Card


class Deck:
    """Deck."""

    def __init__(self):
        """Constructor."""
        self.deck = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        """Convert to string."""
        buffer = ""
        for card in self.deck:
            buffer += str(card) + '\n'
        return buffer

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.deck)

    def deal(self):
        """Deal a card."""
        card = self.deck.pop()
        return card

if __name__ == "__main__":
    print('DECK UNIT TEST')
    test_deck = Deck()
    print('INITIAL DECK')
    print(test_deck)
    print('\nSHUFFLED DECK')
    test_deck.shuffle()
    print(test_deck)
    print('\nDEAL CARDS')
    print(f'Before dealing, deck has {len(test_deck.deck)} cards')
    for i in range(0, 5):
        c = test_deck.deal()
        print(f'Dealt {c}')
    print(f'After dealing, deck has {len(test_deck.deck)} cards')
