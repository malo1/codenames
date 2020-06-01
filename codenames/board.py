"""
This file contains our game board.
It contains 5x5 cards for two teams.
They contain the assassin, agents or none.
"""

RED = 'red'
BLUE = 'blue'
NEUTRAL = 'no_team'
ASSASSIN = 'assassin'


class Card():
    def __init__(self, team: str, word: str):
        self.team = team
        self.word = word


class Board():
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)
