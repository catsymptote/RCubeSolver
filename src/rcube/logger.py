class Logger:
    base_moves = {
        'X': 0,
        'Y': 0,
        'Z': 0,
        'U': 0,
        'E': 0
    }
    all_moves = {
        "U": 0, "U'": 0, "U2": 0, "R": 0, "R'": 0, "R2": 0,  "F": 0, "F'": 0, "F2": 0,  # noqa
        "D": 0, "D'": 0, "D2": 0, "L": 0, "L'": 0, "L2": 0,  "B": 0, "B'": 0, "B2": 0,  # noqa
        "u": 0, "u'": 0, "u2": 0, "r": 0, "r'": 0, "r2": 0,  "f": 0, "f'": 0, "f2": 0,  # noqa
        "d": 0, "d'": 0, "d2": 0, "l": 0, "l'": 0, "l2": 0,  "b": 0, "b'": 0, "b2": 0,  # noqa
        "E": 0, "E'": 0, "E2": 0, "M": 0, "M'": 0, "M2": 0,  "S": 0, "S'": 0, "S2": 0,  # noqa
        "X": 0, "X'": 0, "X2": 0, "Y": 0, "Y'": 0, "Y2": 0,  "Z": 0, "Z'": 0, "Z2": 0,  # noqa
    }

    def log_moves(self, moves):
        for move in moves:
            # if move not in Logger.all_moves:
            #     Logger.all_moves[move] = 0
            Logger.all_moves[move] += 1
            # Logger.all_moves[move] = Logger.all_moves.get(move, 0) + 1

    def print_moves(self, moves=None):
        if moves is None:
            moves = Logger.all_moves

        string = ""
        string += "-" * 27 + "\n"
        string += "#\t  -\t  '\t  2\n"
        string += "-" * 27 + "\n"
        for index in range(0, len(moves), 3):
            key1 = list(moves.keys())[index]
            key2 = list(moves.keys())[index + 1]
            key3 = list(moves.keys())[index + 2]

            string += f"{key1[0]:3}"
            string += f"\t{moves[key1]:3}"
            string += f"\t{moves[key2]:3}"
            string += f"\t{moves[key3]:3}"
            string += "\n"

        return string
