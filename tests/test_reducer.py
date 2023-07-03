from src.reducer import Reducer


def test_init():
    moves = ["R", "U", "R", "U", "R", "R'", "U"]
    expected_moves = ["R", "U", "R", "U2"]

    red = Reducer(moves)
    red.reduce()
    resulting_moves = red.get_moves()

    assert expected_moves == resulting_moves, f"{expected_moves}\n{resulting_moves}"
    print("Success!")
