import codenames.board as board


def test_add_card():
    b = board.Board()
    card = board.Card(board.BLUE, 'helloworld')
    b.add_card(card)
    assert(len(b.cards) == 1)


def test_guess_card_doesnt_exist():
    b = board.Board()
    assert(b.guess('nothere') is None)


def test_guess_card_exists():
    b = board.Board()
    b.add_card(board.Card(board.RED, 'word'))
    assert(b.guess('word') == board.RED)


def test_guess_multiple_cards():
    b = board.Board()
    b.add_card(board.Card(board.RED, 'word'))
    b.add_card(board.Card(board.BLUE, 'another'))
    assert(b.guess('another') == board.BLUE)
