"""
This file contains our game board.
It contains 5x5 cards for two teams.
They contain the assassin, agents or none.
"""
TEAM_RED = 'red'
TEAM_BLUE = 'blue'
NO_TEAM


class Card():
    def __init__(self, team, word):
        self.team = team
        self.word = word



class Board():
    def __init__(self, cardlist, team):
        self.wordlist = wordlist
        self.team = team

def greet(name):

    return f"Oh, Hi {name}"