'''
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
'''

from alg_lookup import AlgLookup


class PochmannTranslator:
    def __init__(self):
        self.alg_lookup = AlgLookup()
        self.setup_moves = {
            'A': ([], 'Ja'),
            'B': ([], 0),
            'C': ([], 'Jb'),
            'D': ([], 'T'),
            'E': (['L', "D'", 'L'], 'T'),
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

        moves = setup + self.alg_lookup.get(alg) + teardown
        return moves


def test():
    pt = PochmannTranslator()
    expected = ["L", "D'", "L",
                "R", "U", "R'", "U'", "R'", "F", "R2", "U'",
                    "R'", "U'", "R", "U", "R'", "F'",
                "L'", "D", "L'"]
    result = pt.translate('E')
    assert expected == result, f'\n{expected}\n{result}'
    print('Success!')


if __name__ == '__main__':
    test()
