"""
Lookup table structure:
    position: (setup, permutation)

Uppercase letters: Edge
Lowercase letters: Corner

Permutations
    T: D
    Ja: A
    Jb: C

    Y: p

    P: R (parity)
"""

from rcube.alg_lookup import AlgLookup


class PochmannTranslator:
    def __init__(self):
        self.alg_lookup = AlgLookup()
        self.setup_moves = {
            "A": ([], "Ja"),
            "B": ([], None),
            "C": ([], "Jb"),
            "D": ([], "T"),
            "E": (["L", "E'", "L"], "T"),
            "F": (["E'", "L"], "T"),
            "G": (["D", "M'"], "Jb"),
            "H": (["E", "L'"], "T"),
            "I": (["M'"], "Ja"),
            "J": (["E2", "L"], "T"),
            "K": (["M'"], "Jb"),
            "L": (["L'"], "T"),
            "M": ([], None),
            "N": (["E", "L"], "T"),
            "O": (["D'", "M'"], "Jb"),
            "P": (["E'", "L'"], "T"),
            "Q": (["M"], "Jb"),
            "R": (["L"], "T"),
            "S": (["D2", "M'"], "Jb"),
            "T": (["E2", "L'"], "T"),
            "U": (["D'", "L2"], "T"),
            "V": (["D2", "L2"], "T"),
            "W": (["D", "L2"], "T"),
            "X": (["L2"], "T"),
            "-": ([], "Ra"),  # Edge parity
            "a": ([], None),
            "b": (["R", "D'"], "Yb"),
            "c": (["F"], "Yb"),
            "d": (["F", "R'"], "Yb"),
            "e": ([""], None),
            "f": (["F2"], "Yb"),
            "g": (["D2", "R"], "Yb"),
            "h": (["D2"], "Yb"),
            "i": (["F'", "D"], "Yb"),
            "j": (["F2", "D"], "Yb"),
            "k": (["F", "D"], "Yb"),
            "l": (["D"], "Yb"),
            "m": (["R'"], "Yb"),
            "n": (["R2"], "Yb"),
            "o": (["R"], "Yb"),
            "p": ([], "Yb"),
            "q": (["R'", "F"], "Yb"),
            "r": ([""], None),
            "s": (["D'", "R"], "Yb"),
            "t": (["D'"], "Yb"),
            "u": (["F'"], "Yb"),
            "v": (["D'", "F'"], "Yb"),
            "w": (["D2", "F'"], "Yb"),
            "x": (["D", "F'"], "Yb")
        }

    def single_invert(self, move):
        if len(move) == 1:
            return move + "'"
        elif move[1] == "'":
            return move[0]
        else:
            return move

    def invert(self, moves):
        inverted_moves = moves[::-1]
        inverted_moves = [self.single_invert(m) for m in inverted_moves]
        return inverted_moves

    def translate(self, letter):
        setup, alg = self.setup_moves[letter]
        teardown = self.invert(setup)

        moves = setup + self.alg_lookup.get_list(alg) + teardown
        return moves
