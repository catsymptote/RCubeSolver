import copy


class MoveTranslator:
    def __init__(self):
        self.lookup = {
            # Single slices
            'U': ['U'],
            'D': ['X', 'X', 'U', 'X', 'X'],
            'R': ['Z', 'Z', 'Z', 'U', 'Z'],
            'L': ['Z', 'U', 'Z', 'Z', 'Z'],
            'F': ['X', 'U', 'X', 'X', 'X'],
            'B': ['X', 'X', 'X', 'U', 'X'],

            # Mid-slices
            'E': ['E'],
            'M': ['Z', 'Z', 'Z', 'E', 'Z'],
            'S': ['X', 'X', 'X', 'E', 'X'],

            # Double slices
            'u': ['U', 'E', 'E', 'E'],
            'd': ['D', 'E'],  # or the other way around? (E and E_.)
            'r': ['R', 'M', 'M', 'M'],
            'l': ['L', 'M'],
            'f': ['F', 'S'],
            'b': ['B', 'S', 'S', 'S'],
        }

    def get_count(self, move):
        assert len(move) in [1, 2]

        if len(move) == 1:
            return 1
        if move[1] == '2':
            return 2
        return 3

    def translate(self, moves: list[str]) -> list[str]:
        moves = copy.copy(moves)

        index = 0
        while index < len(moves):
            move = moves[index]

            # Move translation
            base_move = move[0]
            insert_moves = self.lookup[base_move] * self.get_count(move)
            moves[index : index + 1] = insert_moves[:]
            index += len(insert_moves)
            continue

        return moves
