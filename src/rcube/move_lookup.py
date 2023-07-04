import random


class MoveLookup:
    def __init__(self):
        self.moves = 'URFDLB' + 'EMS' + 'urfdlb'
        self.rotations = 'XYZ'
        self.valid_letters = self.moves + self.rotations
        self.modifiers = ["", "2", "'"]

    def get_random_move(self, include_rotation=False):
        valid_moves = self.moves
        if include_rotation:
            valid_moves += self.rotations
        
        random_move = random.choice(valid_moves)
        random_modifier = random.choice(self.modifiers)
        random_valid_move = random_move + random_modifier
        return random_valid_move

    def is_valid(self, move: str) -> bool:
        if len(move) not in [1, 2]:
            return False

        letter = move[0]
        modifier = ""
        if len(move) == 2:
            modifier = move[1]
    
        return letter in self.valid_letters and modifier in self.modifiers


if __name__ == '__main__':
    ml = MoveLookup()
    print([ml.get_move(True) for _ in range(10)])
