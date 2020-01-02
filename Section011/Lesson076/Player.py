"""Blackjack player."""

import random
from Bank import Bank
from Card import Card
from Hand import Hand


class Player:
    """Player."""

    def __init__(self):
        """Constructor."""
        self.bank = Bank()
        self.hand = Hand()
        self.name = 'Player'

    def take_bet(self):
        """Take the player's bet."""
        bet = 0
        while True:
            buffer = input('How much do you want to bet? ')
            try:
                bet = int(buffer)
                if bet < 0:
                    print('Negative bets are not allowed. Try again.')
                elif bet > self.bank.total:
                    print('You do not have enough for that bet. Try again.')
                else:
                    break
            except:
                print('Invalid input. Try again.')
        return bet

    def hit_or_stand(self):
        """Query if the player wants more cards."""
        while True:
            buffer = input('Do you want another card (Y/N)? ')
            bet = False
            try:
                response = buffer[0].upper()
                if response == 'Y':
                    bet = True
                    break
                elif response == 'N':
                    bet = False
                    break
                else:
                    print('Please type Y or N. ')
            except:
                print('Invalid input. Try again.')
        return bet

    def run_unit_test(self):
        """Run a unit test."""
        max_iters = 5
        iters = 0
        while iters < max_iters and self.bank.total > 0:
            iters += 1
            self.hand.clear()
            bet = self.take_bet()
            if bet < 0:
                print('Player is out of money. Game over.')
                break
            self.bank.bet = bet
            while True:
                hit = self.hit_or_stand()
                if hit:
                    s = random.choice(Card.suits)
                    r = random.choice(Card.ranks)
                    self.hand.add_card(Card(s, r))
                    print(f'Hand: {self.hand.str_some()}')
                else:
                    print(f'Player total = {self.hand.value()}')
                    print(f'Final Hand: {self.hand.str_all()}')
                    break
            won = False
            if self.hand.value() > 21:
                won = False
            else:
                won = random.choice([False, True])
            if won:
                self.bank.win_bet()
                print(f'Player won. Bank={self.bank.total}')
            else:
                self.bank.lose_bet()
                print(f'Player lost. Bank={self.bank.total}')


if __name__ == '__main__':
    player = Player()
    player.run_unit_test()
