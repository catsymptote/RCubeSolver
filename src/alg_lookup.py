"""
Source:
https://www.rubiksplace.com/speedcubing/PLL-algorithms/
"""


class AlgLookup:
    def __init__(self):
        self.str_lookup: dict[str, str] = {
            "T": "(R U R' U') R' F R2 (U' R' U' R) U R' F'",
            "Ja": "[R' U L'] U2 [R U' R' U2] [L R U']",
            "Jb": "[R U R' F'] [R U R' U' R' F] [R2 U' R' U']",
            # 'Y': "[F R U' R' U' R U R' F'] [R U R' U'] [R' F R F']"
            "Yb": "[R U' R' U' R U R' F'] [R U R' U'] [R' F R]",
        }
        self.list_lookup: dict[str, list[str]] = {}
        for perm, alg in self.str_lookup.items():
            self.list_lookup[perm] = self.convert(alg)

    def convert(self, alg: str) -> list[str]:
        removes = "()[]{}"
        for rem in removes:
            alg = alg.replace(rem, "")

        moves = alg.split()
        return moves

    def get_str(self, alg: str) -> str:
        return self.str_lookup[alg]

    def get_list(self, alg: str) -> list[str]:
        return self.list_lookup[alg]
