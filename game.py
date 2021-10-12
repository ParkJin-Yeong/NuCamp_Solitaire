from carddeck import Deck
from displayer import *
from board import *


class Game:
    def __init__(self):
        self.game_deck = Deck()
        self.game_deck.shuffle_Deck()
        self.displayer = Displayer()
        self.board = Board(self.game_deck)

    def play_Game(self):
        self.displayer.display_Game(self.board, self.game_deck)
