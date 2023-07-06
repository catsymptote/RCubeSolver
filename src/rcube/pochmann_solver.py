'''
1. Find shots
2. Find algorithms + setup/teardown (PochmannTranslator)
3. Find moves. (AlgLookup)
'''

from rcube.cube_interface import CubeInterface
from rcube.pochmann_translator import PochmannTranslator
from rcube.alg_lookup import AlgLookup
from rcube.settings import Settings


class PochmannSolver:
    def __init__(self, cube: CubeInterface):
        Settings.use_BLD_notation = True

        self.translator = PochmannTranslator()
        self.alg_lookup = AlgLookup()
        self.cube = cube
        self.touched_buffers = {'edge': False, 'corner': False}

    def get_piece_letters(self, shot):
        pieces = (
            'AQ', 'BM', 'CI', 'DE', 'HR', 'FL', 'JP', 'NT', 'GX', 'KU', 'OV', 'SW',  # noqa: E501
            'aer', 'bqn', 'cmj', 'dif', 'hxs', 'lug', 'pvk', 'two'
        )
        for piece in pieces:
            if shot in piece:
                return piece
        return None

    def is_same_piece(self, sticker1, sticker2):
        piece1 = self.get_piece_letters(sticker1)
        piece2 = self.get_piece_letters(sticker2)
        return piece1 == piece2

    def shot_finished(self, shot, shots):
        # Find flag (*).
        for index, existing_shot in enumerate(shots[:-2]):
            if shot == existing_shot and '*' in existing_shot:
                shots[index] = existing_shot[0]
                break

        for existing_shot in shots:
            piece_letters = self.get_piece_letters(existing_shot)
            if piece_letters and shot in piece_letters:
                return True

        return False

    def get_next_shot_setup(self, shots, corner: bool):
        buffer = 'a' if corner else 'B'

        poss_shots = 'bcdefghijklmnopqrstuvw' if corner \
            else 'ACDEFGHIJKLMNOPQRSTUVWX'

        if (len(shots) == 0) or (corner and shots[-1].isupper()):
            # current_buffer = self.cube[buffer]
            current_buffer = self.cube[buffer]
        else:
            current_buffer = self.cube[shots[-1][0]]

        return poss_shots, buffer, current_buffer

    def get_next_shot(self, shots, corner: bool):
        poss_shots, buffer, current_buffer \
            = self.get_next_shot_setup(shots, corner)
        # print(poss_shots, buffer, current_buffer)

        # Take the shot.
        # if current_buffer != buffer and not self.shot_finished(current_buffer, shots):  # noqa: E501
        if not self.is_same_piece(current_buffer, buffer) and \
                not self.shot_finished(current_buffer, shots):
            return current_buffer

        # New shot loop required.
        for shot in poss_shots:
            if (not self.shot_finished(shot, shots)) and \
                    (shot not in ['a', 'e', 'r', 'B', 'M', self.cube[shot]]):
                return shot + '*'

        return None

        next_shot = self.cube[current_buffer]
        if next_shot == buffer:
            # Find next shot if current shot is in buffer.
            for shot in poss_shots:
                if shot not in shots:
                    next_shot = shot
                    break

        if buffer == next_shot:
            next_shot = None

        # Return None if the edges/corners are solved.
        return next_shot

    def get_pochmann_shots(self):
        shots = []
        parity_index = None

        # Edges
        next_shot = self.get_next_shot(shots, corner=False)
        while next_shot is not None:
            shots.append(next_shot)
            next_shot = self.get_next_shot(shots, corner=False)

        # Parity
        if len(shots) % 2 == 1:
            parity_index = len(shots)

        # Corners
        next_shot = self.get_next_shot(shots, corner=True)
        while next_shot is not None:
            shots.append(next_shot)
            next_shot = self.get_next_shot(shots, corner=True)

        # Add parity
        if parity_index is not None:
            shots.insert(parity_index, '-')

        shots = [shot[0] for shot in shots]
        return shots

    def pochmann_shots_to_algs(self, shots):
        algs = []
        for letter in shots:
            if letter == '-':
                # parity
                pass
        return algs

    def algs_to_moves(self, algs):
        return algs

    def get_solution(self):
        shots = self.get_pochmann_shots()
        algs = self.pochmann_shots_to_algs(shots)
        moves = self.algs_to_moves(algs)
        return moves


if __name__ == '__main__':
    for scramble in [['U'], ['R'], ['F'], ['D'], ['L'], ['B'], 
                     ['U2'], ["U'"], ['R', 'U'],
                     ['L', 'F2', 'R', 'U2', 'F2', "R'", 'F2', 'R', 'F2', 'D2', 'F2', "D'", "R'", "B'", 'U2', "L'", "B'", 'U2', 'R2', "U'", 'B'],  # noqa: E501
                     ['R', 'U', 'F2', 'D', 'L', 'D', 'B'],
                     ]:
        cube = CubeInterface()
        cube.apply_moves(scramble)
        ps = PochmannSolver(cube)
        print(scramble, '\t', ps.get_pochmann_shots())
