"""
Converts algorithms from
(R U R' U') R U
to
["R", "U", "R'", "U'", "R", "U"]

"""


class AlgConverter:
    def __init__(self):
        pass

    def convert(self, alg: str) -> list[str]:
        removes = "()[]{}"
        for rem in removes:
            alg = alg.replace(rem, "")

        moves = alg.split()
        return moves


def test():
    ac = AlgConverter()
    alg = "(R U R' U') R U"
    expected = ["R", "U", "R'", "U'", "R", "U"]
    ac = AlgConverter()
    result = ac.convert(alg)
    assert expected == result, f"\n{expected}\n{result}"
    print("Success!")


if __name__ == "__main__":
    test()
