import codenames.board as board


def test_add_card():
    b = board.Board()
    card = board.Card(board.BLUE, 'helloworld')
    b.add_card(card)
    assert(len(b.cards) == 1)
