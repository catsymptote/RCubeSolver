from src.alg_lookup import AlgLookup


def test_init():
    al = AlgLookup()
    alg = "T"
    expected = [
        "R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'", "R", "U",
        "R'", "F'"
    ]
    al = AlgLookup()
    result = al.get(alg)
    assert expected == result, f"\n{expected}\n{result}"
    print("Success!")
