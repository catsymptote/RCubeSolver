class Algorithm(list):  # type: ignore
    def __init__(self, moves: str | list[str]):
        if type(moves) is str:
            moves = moves.split()
        self.moves = moves

    def __str__(self):
        return ' '.join(self.moves)
