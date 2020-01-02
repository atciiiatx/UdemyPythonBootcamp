"""Player's bankroll."""


class Bank:
    """Bankroll."""

    default_amount = 100

    def __init__(self, amount=default_amount):
        """Constructor."""
        self.total = amount
        self.bet = 0

    def win_bet(self):
        """Win the bet."""
        self.total += self.bet
        self.bet = 0

    def lose_bet(self):
        """Lose the bet."""
        self.total -= self.bet
        self.bet = 0
