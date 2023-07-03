from src.alg_converter import AlgConverter


def test_init():
    ac = AlgConverter()
    alg = "(R U R' U') R U"
    expected = ["R", "U", "R'", "U'", "R", "U"]
    ac = AlgConverter()
    result = ac.convert(alg)
    assert expected == result, f"\n{expected}\n{result}"
    print("Success!")
