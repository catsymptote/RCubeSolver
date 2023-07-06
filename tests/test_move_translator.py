import pytest

from rcube.move_translator import MoveTranslator


def test_init():
    mt = MoveTranslator()
    moves = ["M", "R"]
    expected = ["Z", "Z", "Z", "E", "Z", "Z", "Z", "Z", "U", "Z"]
    result = mt.translate(moves)
    assert result == expected, f"{expected}\n{result}"
    print("Success!")


@pytest.mark.parametrize('moves, exp_moves', [
    (['U'], ['U']),
    (['D'], ['Z', 'Z', 'U', 'Z', 'Z']),
    (['R', 'U'], ['Z', 'Z', 'Z', 'U', 'Z', 'U']),
    (['L', 'F2'], ['Z', 'U', 'Z', 'Z', 'Z', 'Y', 'Y', 'Y', 'U', 'Y', 'Y', 'Y', 'Y', 'U', 'Y']),
    (["U'"], ['U', 'U', 'U']),

])
def test_translate(moves, exp_moves):
    mt = MoveTranslator()
    assert mt.translate(moves) == exp_moves
