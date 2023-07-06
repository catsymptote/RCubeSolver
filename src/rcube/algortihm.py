class Algorithm(list):
    def __init__(self, moves):
        if type(moves) is str:
            moves = moves.split()
        self.moves = moves
