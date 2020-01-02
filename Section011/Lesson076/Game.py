"""Play a game of blackjack."""

from Bank import Bank
from Card import Card
from Deck import Deck
from Hand import Hand
from Player import Player
from Dealer import Dealer


class Game:
    """Blackjack game."""

    player_bet = 0
    player_hand_value = 0

    def player_busts(self):
        """Player went over 21."""
        print('Hand over. House won.')

    def player_wins(self):
        """Handle player winning."""
        print('Game over. Player won!')

    def dealer_busts(self):
        """Handle dealer going over 21."""
        print('Hand over. Player won.')

    def dealer_wins(self):
        """Handle dealer winning."""

    def show_some_cards(self):
        """Display cards of players."""
        for p in self.my_players:
            print(f'Deck for {p.name} : \n{p.hand.str_some()}')

    def start_game(self):
        """Initialize the game."""
        self.my_deck = Deck()
        self.my_deck.shuffle()
        self.my_players = [Player(), Dealer()]
        for player in self.my_players:
            for i in range(0, 2):
                player.hand.add_card(self.my_deck.deal())
        self.show_some_cards()


if __name__ == "__main__":
    game = Game()
    game.start_game()
