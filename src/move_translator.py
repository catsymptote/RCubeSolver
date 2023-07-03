class MoveTranslator:
    def __init__(self):
        self.lookup = {
            # Single slices
            # 'U': ['U'],  # Don't include here
            "D": ["X2", "U", "X2"],
            "R": ["Z_", "U", "Z"],
            "L": ["Z", "U", "Z_"],
            "F": ["X", "U", "X_"],
            "B": ["X_", "U", "X"],
            # Mid-slices
            # 'E': ['E'],  # Don't include here
            "M": ["Z_", "E", "Z"],
            "S": ["X", "E", "X_"],
            # Double slices
            "u": ["U", "E_"],
            "d": ["D", "E"],  # or the other way around? (E and E_.)
            "r": ["R", "M_"],
            "l": ["L", "M"],
            "f": ["F", "S"],
            "b": ["B", "S_"],
        }

    def translate(self, moves: list[str]) -> list[str]:
        base_moves = "XYZUE"
        index = 0
        while index < len(moves):
            move = moves[index]

            # Base case, no translation needed.
            if move[0] in base_moves:
                index += 1
                continue

            # Move translation
            insert_moves = self.lookup.get(move, None)
            if insert_moves:
                moves[index : index + 1] = insert_moves[:]
                index += len(insert_moves)
                continue

            index += 1
        return moves
