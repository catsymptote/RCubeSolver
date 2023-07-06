import pytest

from rcube.pochmann_translator import PochmannTranslator


def test_init():
    pt = PochmannTranslator()
    expected = [
        "L", "E'", "L",
        "R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'", "R", "U", "R'", "F'",
        "L'", "E", "L'",
    ]
    result = pt.translate("E")
    assert expected == result, f"\n{expected}\n{result}"
    print("Success!")


@pytest.mark.parametrize('move, exp_inverse', [
    ("U", "U'"),
    ("U2", "U2"),
    ("U'", "U"),
    ("U", "U'"),
    ("L2", "L2"),
    ("F'", "F")
])
def test_single_invert(move, exp_inverse):
    pt = PochmannTranslator()
    assert pt.single_invert(move) == exp_inverse


@pytest.mark.parametrize('moves, exp_inverse', [
    (["U", "R"], ["R'", "U'"]),
    (["U2", "L"], ["L'", "U2"]),
    (["U'", "F2"], ["F2", "U"]),
    (["U", "R", "R'", "U"], ["U'", "R", "R'", "U'"]),
    (["L2", "F2"], ["F2", "L2"]),
    (["D", "M'"], ["M", "D'"]),
    (["E", "L'"], ["L", "E'"]),
])
def test_invert(moves, exp_inverse):
    pt = PochmannTranslator()
    assert pt.invert(moves) == exp_inverse


def test_translate():
    expected = ["L", "E'", "L", "R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'", "R", "U", "R'", "F'", "L'", "E", "L'"]
    assert PochmannTranslator().translate('E') == expected
