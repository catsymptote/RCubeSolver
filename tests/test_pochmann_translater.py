from rcube.pochmann_translator import PochmannTranslator


def test_init():
    pt = PochmannTranslator()
    expected = [
        "L", "D'", "L",
        "R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'", "R", "U", "R'", "F'",
        "L'", "D", "L'",
    ]
    result = pt.translate("E")
    assert expected == result, f"\n{expected}\n{result}"
    print("Success!")
