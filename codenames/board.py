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
        """
        Adds a card to the board
        """
        self.cards.append(card)

    def guess(self, word: str) -> str:
        """
        For a given word on any of the cards on this board, this function
        will return the team. If the word does not exist, it will return None
        """
        for card in self.cards:
            if card.word == word:
                return card.team
