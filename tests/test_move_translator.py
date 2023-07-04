from rcube.move_translator import MoveTranslator


def test_init():
    mt = MoveTranslator()
    moves = ["M", "R"]
    expected = ["Z_", "E", "Z", "Z_", "U", "Z"]
    result = mt.translate(moves)
    assert result == expected, f"{expected}\n{result}"
    print("Success!")
