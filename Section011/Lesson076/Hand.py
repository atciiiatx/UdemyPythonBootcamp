"""Player's hand of cards."""

from Card import Card


class Hand:
    """Hand of cards."""

    def __init__(self, is_dealer=False):
        """Constructor."""
        self.cards = []
        self.aces = 0
        self.is_dealer = is_dealer

    def clear(self):
        """Clear the deck."""
        self.cards = []
        self.aces = 0

    def str_some(self):
        """Convert to string. Hide 1 dealer card."""
        return self.str_convert()

    def str_all(self):
        """Convert to string. Show all."""
        return self.str_convert(True)

    def str_convert(self, show_all=False):
        """Convert to string."""
        buffer = ""
        i = 0
        for card in self.cards:
            if (not show_all) and (i == 0 and self.is_dealer):
                buffer += 'Hidden\n'
            else:
                buffer += str(card) + '\n'
            i += 1
        return buffer

    def add_card(self, card):
        """Add a card to the deck."""
        self.cards.append(card)
        if card.rank == "Ace":
            self.aces += 1

    def value(self):
        """Determine the max value <= 21 from these cards."""
        # Compute sum of non-aces
        total = 0
        for card in self.cards:
            if card.rank != "Ace":
                total += card.value()
        # Add ace value
        for i in range(0, self.aces):
            total += 11
        ace_reductions = 0
        while total > 21 and ace_reductions < self.aces:
            total -= 10
            ace_reductions += 1
        return total


if __name__ == "__main__":
    print("HAND UNIT TEST")
    dealer_val = [False, True]
    cards_to_add = [
        Card("Clubs", "Two"),
        Card("Diamonds", "Five"),
        Card("Diamonds", "Ace"),
        Card("Spades", "Three"),
        Card("Hearts", "King"),
        Card("Clubs", "Ace"),
        Card("Spades", "Queen"),
    ]
    for dealer in dealer_val:
        hand = Hand(dealer)
        i = 0
        for card in cards_to_add:
            print(f'\nHand {i}')
            hand.add_card(card)
            print(hand.str_some())
            print(f'Value = {hand.value()}')
            i += 1
        print(hand.str_all())
