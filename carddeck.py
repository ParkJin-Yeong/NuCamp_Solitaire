from random import shuffle
from card import Card


class Deck:
    _cards: list

    def __init__(self):
        self._cards = self.create_deck()

    def __str__(self):
        return "\n".join(str(c) for c in self._cards)

    def create_deck(self):
        return [Card(s, v) for s in "CDHS" for v in range(1, 14)]

    def shuffle_Deck(self):
        shuffle(self._cards)

    def draw_card(self):
        return self._cards.pop(0)
