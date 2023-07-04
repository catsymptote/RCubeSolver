from rcube.cube import Cube
from rcube.move_translator import MoveTranslator
from rcube.move_lookup import MoveLookup


class CubeInterface:
    def __init__(self, cube=None):
        self.translator = MoveTranslator()
        self.move_lookup = MoveLookup()

        if cube is None:
            cube = Cube()
        self.cube = cube

    def apply_base_move(self, base_move):
        # Modifier (2 or _)
        counter = 1
        if len(base_move) > 1:
            if base_move[1] == "2":
                counter = 2
            elif base_move[1] == "_" or base_move[1] == "'":
                counter = 3
        base_move = base_move[0]

        # Perform move
        for _ in range(counter):
            # Cube rotations
            if base_move == "X":
                self.cube.X_cube_rotation()
            elif base_move == "Y":
                self.cube.Y_cube_rotation()
            elif base_move == "Z":
                self.cube.Z_cube_rotation()

            # Single slices
            elif base_move == "U":
                self.cube.U_slice_rotation()
            elif base_move == "E":
                self.cube.E_slice_rotation()

    def apply_moves(self, moves):
        base_moves = self.translator.translate(moves)
        for base_move in base_moves:
            self.apply_base_move(base_move)

    def is_complete(self):
        return self.cube.is_complete()

    def show(self):
        self.cube.show()
