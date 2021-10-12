from carddeck import Deck


class Board():

    def deal_Cards(self, deck: Deck):
        return [[deck.draw_card() for i in range(0, j+1)] for j in range(7)]

    def __init__(self, deck: Deck):
        self.rows = self.deal_Cards(deck)
        self.suits = []

    def __str__(self):
        # return "\n".join("|".join(c if not i else "XX" for i, c in enumerate(r)) for r in self.rows)
        # TODO this sucks, refactor it!
        b = ""
        for round in range(7):
            line = ""
            for i in range(round, 7):
                if round == 0:
                    line += " " + str(self.rows[i][round]) + " "
                else:
                    line += " XX "
            b += "    "*round+line+"\n"
        return b
