"""
Source:
https://www.rubiksplace.com/speedcubing/PLL-algorithms/
"""


from src.alg_converter import AlgConverter


class AlgLookup:
    def __init__(self):
        self.alg_converter = AlgConverter()
        str_lookup: dict = {
            "T": "(R U R' U') R' F R2 (U' R' U' R) U R' F'",
            "Ja": "[R' U L'] U2 [R U' R' U2] [L R U']",
            "Jb": "[R U R' F'] [R U R' U' R' F] [R2 U' R' U']",
            # 'Y': "[F R U' R' U' R U R' F'] [R U R' U'] [R' F R F']"
            "Yb": "[R U' R' U' R U R' F'] [R U R' U'] [R' F R]",
        }
        self.lookup = {}
        for perm, alg in str_lookup.items():
            self.lookup[perm] = self.alg_converter.convert(alg)

    def get(self, alg):
        return self.lookup[alg]
