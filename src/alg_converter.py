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
