from src.alg_lookup import AlgLookup


def test_init():
    al = AlgLookup()
    assert type(al) is AlgLookup
    assert type(al.str_lookup) is dict


def test_get_str():
    al = AlgLookup()
    algorithm = "T"
    expected = "(R U R' U') R' F R2 (U' R' U' R) U R' F'"
    result = al.get_str(algorithm)
    assert expected == result, f"\n{expected}\n{result}"
    print("Success!")


def test_get_list():
    al = AlgLookup()
    algorithm = "T"
    expected = [
        "R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'", "R", "U",
        "R'", "F'"
    ]
    result = al.get_list(algorithm)
    assert expected == result, f"\n{expected}\n{result}"
    print("Success!")
