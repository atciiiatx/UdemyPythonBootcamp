"""Blackjack Dealer."""

import random
from Bank import Bank
from Hand import Hand
from Player import Player


class Dealer(Player):
    """Dealer."""

    player_bet = 0

    def __init__(self):
        """Constructor."""
        self.bank = Bank()
        self.hand = Hand(True)
        self.name = 'Dealer'

    def take_bet(self):
        """Take the dealer's bet."""
        if self.bank.total >= Dealer.player_bet:
            return Dealer.player_bet
        else:
            return -1

    def hit_or_stand(self):
        """Query if the player wants more cards."""
        if self.hand.value() < 17:
            return True
        else:
            return False


if __name__ == '__main__':
    dealer = Dealer()
    Dealer.player_bet = 50
    dealer.run_unit_test()
